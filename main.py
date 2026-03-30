import argparse


def main():
    parser = argparse.ArgumentParser(description='Document Summarizer')
    parser.add_argument('--file', type=str, required=True, help='Path to the input file')
    parser.add_argument('--output', type=str, required=True, help='Path to save the output summary')

    args = parser.parse_args()

    # Add your summarization code here
    # For example, read the file and summarize its content
    input_file_path = args.file
    output_file_path = args.output
    
    # Simulating reading file content 
    with open(input_file_path, 'r') as file:
        content = file.read()
    
    # Simulating summary process (to be replaced with actual logic)
    summary = content[:100]  # just a placeholder for content summarization
    
    with open(output_file_path, 'w') as output_file:
        output_file.write(summary)


if __name__ == '__main__':
    main()