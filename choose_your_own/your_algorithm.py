#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from time import time

clfs = [
    GaussianNB(), 
    SVC(kernel='rbf', C=1000000), 
    DecisionTreeClassifier(), 
    KNeighborsClassifier(n_neighbors=8), 
    RandomForestClassifier(), 
    AdaBoostClassifier()
]

accuracies = {}

for clf in clfs:
    name = clf.__class__.__name__
    print(name)
    
    t0 = time()
    clf = clf.fit(features_train, labels_train)
    print("Training Time:" + str(round(time()-t0, 3)) + "s")

    t0 = time()
    pred = clf.predict(features_test)
    print("Predicting Time:" + str(round(time()-t0, 3)) + "s")

    accuracy = accuracy_score(labels_test, pred)
    print('Accuracy: ' + str(accuracy) + '\n')

    accuracies[clf] = accuracy

    try:
        prettyPicture(clf, features_test, labels_test, name)
    except NameError:
        pass

best_classifier = max(accuracies, key=accuracies.get)
best_accuracy = accuracies[best_classifier]

print('Best Classifier: ' + repr(best_classifier))
print('Best Accuracy: ' + repr(best_accuracy))
