from spellchecker import SpellChecker
import os

# Create a spell checker instance
spell = SpellChecker()

# Directory where txt file(s) (containing only filtered words without punctuation and symbol) exist
input_dir = './data-directory/cleaned/'

# Directory where new txt file(s) will get generated containing misspelled words
output_dir = './data-directory/spell-checked/'

# Loop through all the txt files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # Open the input file for reading
        with open(os.path.join(input_dir, filename), 'r') as f:
            # Read the contents of the file
            contents = f.read()

        # Split the contents into words
        words = contents.split()

        # Create a list of words to skip
        skip_words = ['Fynd', 'checkouts', 'integrations', 'CSS', 'vv', 'navbar', 'svg', 'webpage', 'webpages', 'www', 'fyndstore', 'sub', 'navig', 'Shopsense',
              'programme', 'colour', 'favourite', 'centre', 'neighbour', 'behaviour', 'realise', 'customise', 'analyse', 'organise', 'recognise', 'ios', '#madeinindia', 'openapi', 'boltic', 'pixelbin']
        skip_words = [word.lower() for word in skip_words]

        # Create an empty list to store misspelled words
        misspelled = []

        # Check each word for spelling errors
        for word in words:
            # Check if the word is in the list of skip words
            if word.lower() in skip_words:
                continue
            # Check if the word is a single letter
            if len(word) <= 2:
                continue
            # Check if the word is misspelled
            if word not in spell:
                # Add the misspelled word to the list
                misspelled.append(word)

        # Write the misspelled words to the output file
        output_filename = os.path.splitext(filename)[0] + '-spellchecked.txt'
        with open(os.path.join(output_dir, output_filename), 'w') as f:
            f.write('\n'.join(misspelled))

        # Print a message to indicate completion
        print(f'Misspelled words identified and written to {os.path.join(output_dir, output_filename)}')
