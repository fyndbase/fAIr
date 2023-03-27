# User Guide for fAIr Typo Detector 

## Overview

### What it does?
Identifies a typo in a snapshot (png/jpg) and draws a red border around each of the misspelled words. 

(If you want to quickly test, a sample image exists in the **input** folder containing a few spelling mistakes. Run `sh run_scripts.sh` to check the output)

### Pros
* Reviews multiple snapshots at once
* Saves manual efforts

### Cons
* Slow rendering
* False positives

### Tech
* Python
* OpenCV
* Tesseract OCR

---

## Steps

1. Open the project folder named **fAIr** (your cloned repo directory on the PC) using a code editor/IDE (say VS Code).

2. Put all you image files (preferably of high resolution) in the directory named **input** (present inside fAIr directory).

3. While being in the same directory, run the following command: `sh run_scripts.sh`.

OpenCV will display an image viewer where all the typos (present in that image) would be highlighted. To move to the next image, click **Enter**.

> **Note**: The processing might take some time, so kindly bear with us until the code is optimised.

---

## Purpose of each file

* **run_scripts.sh** - Shell script to run the entire code systematically.

* **src/word-extract.py** - Extracts all the words present in an image, and lists it in a text file (1st level processing).

* **src/clean-extract.py** - 2nd level processing to remove punctuations and symbols to be considered as a word.

* **src/spell-check.py** - 3rd level processing that conducts an actual spell-check and identifies misspelled words. Contains a list of exceptions too.

* **src/final-files.py** - A program that renames the txt files generated by `spell-check.py`. Currently, this program exists only for making it easier for `locator.py` to map (filenames of images) to (filenames of txt files) for direct comparison. This file will be removed in future as it can be handled better in `locator.py`.

* **src/locator.py** - Uses OpenCV to identify the co-ordinates of misspelled words.

* **input (*folder*)** - Folder for your image files. Put your png/jpg files in this folder.

* **data-directory** - Directory used by the project to generate intermediate files during execution of code.