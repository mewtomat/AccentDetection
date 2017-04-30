#! /bin/bash
# $1 is the directory containing the mp3 files
#$2 target directory
for file in `ls $1/*.mp3`;do
	echo "$file"
	filename="${file##*/}"
	filename="${filename%%.*}"
	if [ ! -f "$2"/"$filename".wav ]; then
		mpg321 -w "$2"/"$filename".wav "$file"
	fi
done