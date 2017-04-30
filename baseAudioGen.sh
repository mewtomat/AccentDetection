# rm -rf StandardWords

# mkdir StandardWords

for word in `cat utt_dict`;
do
	formatted=`echo $word | tr -dc '[:alnum:]' | tr  '[:lower:]' '[:upper:]'`
	# espeak --stdout "$formatted" >> ./StandardWords/"$formatted".wav
	echo "hihi"
	# echo "$formatted" | text2wave -o ./StandardWords/"$formatted".wav
	# espeak "$formatted" -w ./StandardWords/"$formatted".wav
	python convert_mfcc.py ./StandardWords/"$formatted".wav ./StandardWords/"$formatted".mfcc
done