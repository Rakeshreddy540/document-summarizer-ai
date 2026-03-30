# Configuration settings for Document Summarizer AI

# Model Names
MODEL_NAMES = {
    'bert': 'bert-base-uncased',
    'gpt3': 'gpt-3.5-turbo',
}

# Output Formats
OUTPUT_FORMATS = ['text', 'json']

# Summarization Parameters
SUMMARIZATION_PARAMS = {
    'min_length': 50,
    'max_length': 150,
    'temperature': 0.7,
}