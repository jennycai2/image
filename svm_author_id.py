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

import skimage

from skimage.measure import structural_similarity as ssim
##import cv2
from compare_images import CompareImages
#from compare_images import GreyScale
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

### change one image to grey-scale

"""
image16 = "16_left_mirror_grey.jpeg"
image16_ = "16_right_grey.jpeg"
image17 = "17_left_mirror_grey.jpeg"
image17_ = "17_right_grey.jpeg"
image1 = pil.open(image16)
image2 = pil.open(image16_)
"""
#s = ssim(image1, image2)
#print s

#print CompareImages("10_left_grey_mirror.jpeg", "10_left_grey_mirror.jpeg")
print CompareImages("10_left_grey_mirror.jpeg", "10_right_grey.jpeg")
#print CompareImages("10_left_grey.jpeg", "10_right_grey.jpeg")

print CompareImages("13_left_grey_mirror.jpeg", "13_right_grey.jpeg")
print CompareImages("15_left_grey_mirror.jpeg", "15_right_grey.jpeg")
print CompareImages("16_left_grey_mirror.jpeg", "16_right_grey.jpeg")
print CompareImages("17_left_grey_mirror.jpeg", "17_right_grey.jpeg")

#print CompareImages(image17, image17_)

#GreyScale()
print "good"
for image in glob.glob("*.jpeg"):
    #print image
    myimage = pil.open(image)

    grey = myimage.convert('L') ### convert to grey-scale
    grey=np.asarray(grey,dtype=np.uint8)  #if values still in range 0-255!
    w=pil.fromarray(grey,mode='L') ### convert back to image
    outfilename = os.path.splitext(os.path.basename(image))[0]+'_grey.jpeg'
    #w.save(outfilename)



    mirror = w.transpose(pil.FLIP_LEFT_RIGHT)
    outfilename = os.path.splitext(os.path.basename(image))[0]+'_mirror.jpeg'
    #mirror.save(outfilename)



    im=pil.open(image)
    width, height = im.size
    if image.endswith('.jpeg'):
       image = image[:-5]
    row = [[image, width, height, float(width)/float(height)]]
    wr.writerows(row)


"""
>>> import scipy as sp
>>> from scipy.misc import imread
>>> from scipy.signal.signaltools import correlate2d as c2d
>>>
>>> def get(i):
...     # get JPG image as Scipy array, RGB (3 layer)
...     data = imread('im%s.jpg' % i)
...     # convert to grey-scale using W3C luminance calc
...     data = sp.inner(data, [299, 587, 114]) / 1000.0
...     # normalize per http://en.wikipedia.org/wiki/Cross-correlation
...     return (data - data.mean()) / data.std()
...
>>> im1 = get(1)
>>> im2 = get(2)
>>> im3 = get(3)
>>> im1.shape
(105, 401)
>>> im2.shape
(109, 373)
>>> im3.shape
(121, 457)
>>> c11 = c2d(im1, im1, mode='same')  # baseline
>>> c12 = c2d(im1, im2, mode='same')
>>> c13 = c2d(im1, im3, mode='same')
>>> c23 = c2d(im2, im3, mode='same')
>>> c11.max(), c12.max(), c13.max(), c23.max()
(42105.00000000259, 39898.103896795357, 16482.883608327804, 15873.465425120798)
"""
