#!/bin/bash

# the first arguement is the directory containing the wav files
# second arguement is the text file containing the transcript

set -x

present_dir=`pwd`

cp $2 $1/

cd $1 || exit 1

rm -f *.scp utt2spk spk2utt text

for file in `ls *.wav`;
do 
	freq=`soxi $file | sed '4!d;q' | cut -d' ' -f7`
	if [ $freq -ne 44100 ];then
		echo "Moving $file"
		mv $file ./Extras/
	else
		uttid="${file%%.*}"
		echo "$uttid" $PWD/$file >> wav.scp
		echo "$uttid" "$uttid" >> utt2spk 
		echo "$uttid" "$uttid" >> spk2utt 
		echo -n "$uttid " >>text
		cat $2 >>text
		echo >>text
	fi
done

rm $2
cd $present_dir

utils/fix_data_dir.sh "$1"