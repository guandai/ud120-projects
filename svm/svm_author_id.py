#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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




#########################################################
### your code goes here ###

from sklearn.svm import SVC
clf = SVC(kernel="rbf", C=10000)


#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data
features_train = features_train[:len(features_train)] 
labels_train = labels_train[:len(labels_train)] 

clf.fit(features_train, labels_train)

#### store your predictions in a list named pred

# pred1 = clf.predict(features_test[10])
# pred2 = clf.predict(features_test[26])
# pred3 = clf.predict(features_test[50])

# print(pred1)  # 1
# print(pred2)  # 0
# print(pred3)  # 1

from sklearn.metrics import accuracy_score
pred = clf.predict(features_test)
acc = accuracy_score(pred, labels_test)
print(len(filter(lambda x: x==1, pred))) #// 877

#########################################################


