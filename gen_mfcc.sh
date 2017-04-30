#! /bin/bash

mkdir -p mfcc_new

for words in `ls words_new`
do
	mkdir -p mfcc_new/"$words"
	for files in `ls words_new/"$words/"`
	do
		python convert_mfcc.py ./words_new/"$words"/"$files" ./mfcc_new/"$words"/"$files"
	done
done