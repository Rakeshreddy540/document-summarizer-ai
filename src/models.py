import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

class SummarizationModel:
    def __init__(self, model_name="t5-base"):
        self.model_name = model_name
        self.tokenizer = T5Tokenizer.from_pretrained(self.model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(self.model_name)

    def load_model(self):
        # Load the pre-trained model and tokenizer
        return self.model, self.tokenizer

    def summarize(self, text):
        # Tokenize the input text
        input_ids = self.tokenizer.encode(text, return_tensors="pt")
        # Generate summary
        summary_ids = self.model.generate(input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        # Decode the generated summary
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary

# Example usage:
# summarizer = SummarizationModel()
# model, tokenizer = summarizer.load_model()
# summary = summarizer.summarize("Your text here...")
