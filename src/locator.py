import pytesseract
import cv2
import os

# Directory where renamed txt file(s) exist (same as image name)
input_dir = './data-directory/final'

# Directory where txt log files will be created containing successfully located misspelled words
output_dir = './data-directory/input'

# Loop through all the txt files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.txt'):
        # Open the input file for reading
        with open(os.path.join(input_dir, filename), 'r') as f:
            # Read the contents of the file
            contents = f.read()

        # Split the contents into words
        words = contents.split()

        # Load the image
        image_file = filename.replace('.txt', '.png')
        image_path = os.path.join('input', image_file)
        img = cv2.imread(image_path)

        # Increase the image resolution by 3 times
        scale_percent = 300  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        img = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)

        # Find the coordinates of the misspelled words in the image
        found_words = []
        d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        for i, word in enumerate(d['text']):
            word = word.strip()
            for misspelled_word in words:
                if misspelled_word in word:
                    x, y, w, h = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
                    margin = 20
                    cv2.rectangle(img, (x - margin, y - margin), (x + w + margin, y + h + margin), (0, 0, 255), thickness=10)
                    found_words.append(misspelled_word)

        # Print whether the misspelled words were found in the image or not
        if found_words:
            print(f"The following misspelled words were found in the image {image_file}: {', '.join(found_words)}")
            # Display the image with misspelled words highlighted
            cv2.imshow('Misspelled Words', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
