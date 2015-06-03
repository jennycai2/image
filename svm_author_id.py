#!/usr/bin/python

"""
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors

    Sara has label 0
    Chris has label 1

"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

import glob, os




### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
"""
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

#########################################################

from sklearn.svm import SVC

    ### create classifier
###clf = SVC(kernel="linear")
### C = 10, 100, 1000, 10000

clf = SVC(kernel="rbf", C=10000.0)


clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
cnt = 0
for p in pred:
	if p==1:
		cnt=cnt+1


print cnt
###print pred[10]
###print pred[26]
###print pred[50]

    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example,
    ### where we just print the accuracy
    ### you might need to import an sklearn module
from sklearn.metrics import accuracy_score
print accuracy_score(pred, labels_test)
"""

### find image size
from PIL import Image as pil

### write a .csv file
import csv
import matplotlib.pyplot
import pylab


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

"""
fig = plt.figure()

ax1 = fig.add_subplot(111)

data = np.genfromtxt('output.csv', delimiter=',', names=['n', 'x', 'y'])

ax1.plot(data['x'], data['y'], color='r', label='the data')
leg = ax1.legend()

plt.show()

"""
wr = csv.writer(open("output.csv",'wb'))
###os.chdir("../../Downloads/train")
###os.chdir("../../Downloads/sample")

for image in glob.glob("*.jpeg"):

    myimage = pil.open(image)

    """
    mirror = myimage.transpose(pil.FLIP_LEFT_RIGHT)
    outfilename = os.path.splitext(os.path.basename(image))[0]+'_r90.jpeg'
    mirror.save(outfilename)
    """

    im=pil.open(image)
    width, height = im.size
    if image.endswith('.jpeg'):
       image = image[:-5]
    row = [[image, width, height, float(width)/float(height)]]
    wr.writerows(row)
