import numpy as np
import os
import random
import glob
import scipy.io.wavfile
from scikits.talkbox.features import mfcc
import sys

nations=[]

nation_file = open("nationalities","r")
for line in nation_file.readlines():
	line=line.strip()
	nations=np.append(nations,line)

for word in os.listdir('./words_new'):
	print "doing ", word
	if not os.path.exists("./mfcc_new_2/"+word):
		os.makedirs("./mfcc_new_2/"+word)
	for nation in nations:
		print "doint ", nation
		file_list = glob.glob("./words_new/"+word+"/"+nation+"*")
		print "./words_new/"+word+"/"+nation+"*"
		try:
			index = random.randint(0,len(file_list)-1)
			sample_rate, X = scipy.io.wavfile.read(file_list[index])
			ceps, mspec, spec = mfcc(X)
			feats = np.concatenate((ceps,mspec),axis=1)
			np.save("mfcc_new_2/"+word+"/"+nation, feats)	
		except:
			print "skipping "+nation+" in "+word
			continue



