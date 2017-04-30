
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
import sys
import os
from sklearn.cross_validation import train_test_split


trainingDir="mfcc_new_2/"

StandardWords = dict()

for f in os.listdir('./StandardWords'):
    split_f = f.split(".")
    if(len(split_f)==3 and split_f[2]=="npy"):
        print "Doing for ", f
        StandardWords[split_f[0]] = np.load("./StandardWords/"+f)
        print StandardWords[split_f[0]].shape

feats = np.zeros((1,13*2))
data = ["reference"]

for word in os.listdir(trainingDir):
    print "Doing ", word
    for nationality in os.listdir(trainingDir+word+"/"):
        # print "Doing ", nationality
        try:
            curr = np.load(trainingDir+word+"/"+nationality)
            curr = curr[:,[0,1,2,3,4,5,6,7,8,9,10,11,12]]
            # curr_tmp = curr.reshape((53,curr.shape[0]))
            # curr_tmp = curr_tmp[0:13]
            # curr = curr_tmp.reshape(())
            curr_delta = curr - StandardWords[word]
            where_are_NaNs = np.isinf(curr_delta)
            curr_delta[where_are_NaNs] = np.nan
            mean_curr = np.nanmean(curr_delta,axis=0)
            std_curr = np.nanstd(curr_delta,axis=0)
            feats_curr = np.concatenate((mean_curr,std_curr))
            feats_curr = feats_curr.reshape((1,26))
            feats = np.concatenate((feats,feats_curr))
            nation=nationality.replace(".wav", "")
            data = np.append(data,nation)
            if data.shape[0] != feats.shape[0]:
                print "!!!!!!!!!"
                print data.shape, feats.shape
                wait
        except:
            print "ditching ", nationality , " in ", word

where_are_NaNs = np.isinf(feats)
feats[where_are_NaNs] = 0
where_are_NaNs = np.isnan(feats)
feats[where_are_NaNs] = 0

n_neighbors = 15

X=feats
y=data

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)


# for weights in ['uniform', 'distance']:
#     for n_neighbors in [2,4,6,8,10,15,20,25,30,40,50]:
#         clf = neighbors.KNeighborsClassifier(n_neighbors, weights="uniform")
#         clf.fit(X_train, y_train)
#         score=clf.score(X_test,y_test)
#         print "weights: ", weights, " neighbors: ", n_neighbors, " score: ", score

# from sklearn.tree import DecisionTreeClassifier

# clf = DecisionTreeClassifier(random_state=0)
# clf.fit(X_train, y_train)
# clf.score(X_test, y_test)


# from sklearn.ensemble import GradientBoostingClassifier
# clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=1, random_state=0).fit(X_train, y_train)
# clf.score(X_test,y_test)

# from sklearn.ensemble import RandomForestClassifier
# clf = RandomForestClassifier(n_estimators=10,max_depth=3, random_state=0,n_jobs=2).fit(X_train, y_train)
# clf.score(X_test,y_test)

from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(hidden_layer_sizes=(600,300),solver='adam', alpha=1e-4,max_iter=500).fit(X_train,y_train)
clf.score(X_test,y_test)