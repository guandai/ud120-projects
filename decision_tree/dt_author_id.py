#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

import numpy as np

t0 = time()

print(len(features_train[0]))
# features_train = np.array(features_train).transpose()
# features_train = features_train[:len(features_train)].transpose()

# features_train = np.array(features_train)


features_train = features_train[:len(features_train)] 
labels_train = labels_train[:len(labels_train)] 

#########################################################
### your code goes here ###
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=1000)
clf = clf.fit(features_train, labels_train)

pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print(acc)

print "time:", round(time()-t0, 3), "s"
# print(len(filter(lambda x: x==1, pred))) #// 877
# print(len(filter(lambda x: x!=1, pred))) #// 877
#########################################################


