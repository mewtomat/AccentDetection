#!/bin/bash
. ./path.sh  || die "path.sh expected";

set -x

# $1 is the data directory
# $2 is the transcript

nj=1

stage=3
mfcc_dir=mfcc
alignments_dir=alignments
standard_words=StandardWords/

if [ $stage -le 1 ]; then
	rm -rf $mfcc_dir
	./steps/make_mfcc.sh --nj $nj --cmd "run.pl" "$1" $mfcc_dir/make_mfcc $mfcc_dir
	./steps/compute_cmvn_stats.sh "$1" $mfcc_dir/make_mfcc $mfcc_dir
fi

if [ $stage -le 2 ]; then
	rm -rf $alignments_dir "$1"/split1 utterance.ctm
	./steps/align_si.sh --nj $nj --cmd "run.pl" \
	     "$1" ./data/lang ./exp/tri2a ./$alignments_dir
	$KALDI_ROOT/src/bin/ali-to-phones --ctm-output ./$alignments_dir/final.mdl ark:"gunzip -c $alignments_dir/ali.*.gz|" utterance.ctm
fi

if [ $stage -le 3 ]; then
	rm -rf words_new
	mkdir words_new
	find "$1/" -iname "*.wav" | while read audio;do
	# for audio in `ls "$1"/*.wav`;do
		echo "Splittting file $audio"
		uttid_path="${audio%%.*}"
		uttid=`echo "$uttid_path" | rev | cut -d '/' -f1 | rev`
		# uttid="${uttid_path##*/}"
		if [ ! -f $PWD/words_new/A/"$uttid".wav ];then
			awk -v var="$uttid" '$1 == var { print $0 }' utterance.ctm > this_utterance
			./phone-to-wav.sh "$audio" this_utterance ./data/lang/phones/word_boundary.int words_new "$2" "$standard_words"
		fi
	done
fi