import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc
import sys

sample_rate, X = scipy.io.wavfile.read(sys.argv[1])
ceps, mspec, spec = mfcc(X)
# feats = np.concatenate((ceps),axis=1)
np.save(sys.argv[2], ceps)