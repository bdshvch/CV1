import numpy as np
import tensorflow as tf
from keras.datasets import mnist
from matplotlib import pyplot
import numpy as np
import random
from toimport import FirstStep
from toimport import SecondStep
from toimport import ThirdStep

(trainX, trainY), (testX, testY) = mnist.load_data()

N = 500 #number of test imgs
Size = 28 #only for doctest

def norm(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            if (img[i][j] > 0):
                img[i][j] = 1
            else:
                img[i][j] = 0
    return img

train_filter = np.where((trainY == 0 ) | (trainY == 1))
test_filter = np.where((testY == 0) | (testY == 1))

trainX, trainY = trainX[train_filter], trainY[train_filter]
testX, testY = testX[test_filter], testY[test_filter]


#------------------------------------------------------------------------------#

pr_k_x0 = []
for i in range(N):
    pr_k_x0.append(random.random())


pr_k_x1 = []
for i in range(len(pr_k_x0)):
    pr_k_x1.append(1 - pr_k_x0[i])


pr_k = []

pi0 = []
pi1 = []

for i in range(28):
    temp0 = []
    temp1 = []
    for j in range(28):
        temp0.append(0)
        temp1.append(0)       
    pi0.append(temp0)
    pi1.append(temp1)

#------------------------------------------------------------------------------#

NormTrainX = []

for i in range(N):
    NormTrainX.append(norm(trainX[i]))

def Algorithm(pr_k_x0, pr_k_x1, pi0, pi1, NormTrainX):
    for iter in range(5):
        pr_k = []
        pr_k = FirstStep(pr_k_x0, pr_k_x1)
        pi0, pi1 = SecondStep(pr_k_x0, pr_k_x1, NormTrainX, N, pi0, pi1, Size)
        pr_k_x0, pr_k_x1 = ThirdStep(pi0, pi1, N, pr_k, NormTrainX, Size)
    return 0
    
Algorithm(pr_k_x0, pr_k_x1, pi0, pi1, NormTrainX)

