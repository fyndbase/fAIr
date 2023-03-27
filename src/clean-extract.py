import re
import os

# Directory the location of the txt file(s) containing all words present in the image
input_dir = './data-directory/extracted'

# Directory where new txt file(s) will get generated containing only filtered words without punctuation and symbol
output_dir = './data-directory/cleaned'

# Get a list of all txt files in the input directory
input_files = [f for f in os.listdir(input_dir) if f.endswith('.txt')]

# Process each input file
for input_file in input_files:
    # Construct the full path of the input file
    input_path = os.path.join(input_dir, input_file)

    # Construct the full path of the output file
    output_file = os.path.splitext(input_file)[0] + '-cleaned.txt'
    output_path = os.path.join(output_dir, output_file)

    # Open the input and output text files
    with open(input_path, 'r') as f_input, open(output_path, 'w') as f_output:
        # Read the contents of the input file
        contents = f_input.read()

        # Split the contents into words using regular expressions
        words = re.findall(r'\b\w+\b', contents)

        # Create an empty list to store words without punctuations or symbols
        clean_words = []

        # Check each word for punctuations or symbols
        for word in words:
            # Check if the word contains any punctuations or symbols
            if word.isalpha():
                # Add the clean word to the list
                clean_words.append(word)

        # Write the clean words to the output file
        f_output.write(' '.join(clean_words))

    # Print a message to indicate completion
    print(f'Clean words without unneccesary symbols and punctuations written {output_file} in {output_dir}')
