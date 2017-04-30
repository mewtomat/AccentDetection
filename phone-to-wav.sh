#!/bin/bash

# first arguement is wav file
# second arguement is ctm file
# third arguement is word_boundary.int 
# fourth arguement is directory to place the word files
# fifth arguement is transcript
# sixth arguement is directory of standard words

# set -v

wav=$1
ctm=$2
wbound=$3
transcript=$5

uttid="${wav##*/}"
uttid="${uttid%%.*}"
echo "uttid is $uttid"
cat "$ctm" | grep "$uttid" | awk '{print $3,$4,$5}' > tmp
python break_word.py "$wbound" tmp > tmp2

stringVar=`cat "$transcript"`
arrayVar=(${stringVar// / })

wordNum=0
while read line
do
	start=$(echo $line | awk '{print $1}')
	end=$(echo $line | awk '{print $2}')
	printf -v filenum "%03d" $wordNum
	mkdir -p "$4"/"${arrayVar[$wordNum]}"/
	actual_word="${arrayVar[$wordNum]}"
	sox "$wav" "$4"/$actual_word/"$uttid".tmp.wav trim "$start" "$end"
	length_target=`soxi -D $6/$actual_word.wav `
	length_actual=`soxi -D "$4"/$actual_word/"$uttid".tmp.wav`
	ratioReq=`bc -l <<< "$length_actual/$length_target"`
	if [ $(bc <<< "$ratioReq >= 0.1 && $ratioReq <=10") -eq 1 ]
    then
		sox "$4"/$actual_word/"$uttid".tmp.wav "$4"/$actual_word/"$uttid".wav tempo $ratioReq 30
	fi
	rm "$4"/$actual_word/"$uttid".tmp.wav
	wordNum=$((wordNum+1))
done < tmp2

# rm tmp tmp2