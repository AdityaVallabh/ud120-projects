#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
clf = GaussianNB()

t0 = time()
clf.fit(features_train, labels_train)
print("Training Time:" + str(round(time()-t0, 3)) + "s")

t0 = time()
pred = clf.predict(features_test)
print("Predicting Time:" + str(round(time()-t0, 3)) + "s")

accuracy = accuracy_score(labels_test, pred)
print('Accuracy: ' + str(accuracy))

"""
Training Time:0.962s
Predicting Time:0.117s
Accuracy: 0.9732650739476678
"""

#########################################################


