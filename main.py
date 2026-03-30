import argparse
from transformers import pipeline

def summarize_with_ai(text):
    """Summarize text using a pre-trained transformer model"""
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        # Split text into chunks if too long (max 1024 tokens)
        words = text.split()
        chunks = [' '.join(words[i:i+200]) for i in range(0, len(words), 200)]
        
        summaries = []
        for chunk in chunks:
            if len(chunk.split()) > 50:  # Only summarize if chunk is long enough
                summary = summarizer(chunk, max_length=150, min_length=50, do_sample=False)
                summaries.append(summary[0]['summary_text'])
        
        return ' '.join(summaries) if summaries else text[:200]
    except Exception as e:
        print(f"AI summarization failed: {e}. Using fallback method.")
        return text[:200]


def main():
    parser = argparse.ArgumentParser(description='Document Summarizer AI')
    parser.add_argument('--file', type=str, required=True, help='Path to the input file')
    parser.add_argument('--output', type=str, required=True, help='Path to save the output summary')

    args = parser.parse_args()

    input_file_path = args.file
    output_file_path = args.output
    
    # Read file content
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        return
    
    # Generate summary using AI
    summary = summarize_with_ai(content)
    
    # Write summary to output file
    with open(output_file_path, 'w') as output_file:
        output_file.write(summary)
    
    print(f"Summary saved to {output_file_path}")


if __name__ == '__main__':
    main()