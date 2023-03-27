import os
import shutil

# Directory where new txt file(s) containing misspelled words exist
input_dir = './data-directory/spell-checked/'

# Directory where renamed txt file(s) will get generated
output_dir = './data-directory/final'

# Loop through all the txt files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # Create the new filename by removing '-cleaned-spellchecked' from the original filename
        new_filename = filename.replace('-cleaned-spellchecked', '')

        # Copy the file to the output directory with the new filename
        shutil.copy2(os.path.join(input_dir, filename), os.path.join(output_dir, new_filename))

        # Print a message to indicate completion
        print(f'{filename} renamed to {new_filename} and placed in {output_dir}')