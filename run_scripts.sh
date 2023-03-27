#!/bin/bash

DIR="data-directory"
if [ -d "$DIR" ];
then
    rm -rf data-directory
    mkdir data-directory
else
	mkdir data-directory
fi

mkdir data-directory/{extracted,cleaned,spell-checked,final}

python3 src/word-extract.py
python3 src/clean-extract.py
python3 src/spell-check.py
python3 src/final-files.py
python3 src/locator.py

