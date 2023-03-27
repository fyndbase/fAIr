#!/bin/bash

rm -rf ./data-directory/*
mkdir data-directory
mkdir ./data-directory/extracted/ ./data-directory/cleaned/ ./data-directory/spell-checked/ ./data-directory/final/

python3 src/word-extract.py
python3 src/clean-extract.py
python3 src/spell-check.py
python3 src/final-files.py
python3 src/locator.py

