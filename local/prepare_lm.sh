#!/bin/bash
# Apache 2.0

set -e -o pipefail

. ./path.sh || die "path.sh expected";

local/train_lms_srilm.sh --train-text data/train/text data/ data/srilm

nl -nrz -w10  corpus/LM/train.txt | utils/shuffle_list.pl > data/local/external_text
local/train_lms_srilm.sh --train-text data/local/external_text data/ data/srilm_external

[ -d data/lang_test/ ] && rm -rf data/lang_test
cp -R data/lang data/lang_test
lm=data/srilm/lm.gz

local/arpa2G.sh $lm data/lang_test data/lang_test

exit 0;
