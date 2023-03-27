import pytesseract
from PIL import Image
from PIL import ImageFilter
import os

# Define the directory where the images exist
input_dir = "./input"

# Directory where the txt file(s) will get generated containing all words present in the image
output_dir = "./data-directory/extracted"

# Loop through all PNG files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.png'):
        # Load the image
        img = Image.open(os.path.join(input_dir, filename))

        # Enlarge the image
        # img = img.convert('L')
        img = img.resize((img.width * 5, img.height * 5))

        # Extract the text from the image using Tesseract OCR
        text = pytesseract.image_to_string(img)

        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Write the text to a new file with the same name as the image
        output_filename = os.path.splitext(filename)[0] + '.txt'
        with open(os.path.join(output_dir, output_filename), 'w') as f:
            f.write(text)

        # Print a message to indicate completion
        print(f'{filename} was processed and words extracted to {output_filename} in {output_dir}')
