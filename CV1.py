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

#------------------------------------------------------------------------------#

M = 100 #number of test imgs

NormTestX = []
for i in range(M):
    NormTestX.append(norm(testX[i]))

pr_k_test = []
pr_k_x0_test = []
pr_k_x1_test = []

for i in range(M):
    pr_k_x0_test.append(random.random())
for i in range(M):
    pr_k_x1_test.append(1 - pr_k_x0_test[i])

pr_k_test = FirstStep(pr_k_x0_test, pr_k_x1_test)


Prob0 = [] #Probability for each img to be in first claster
Prob1 = [] #Probability for each img to be in second claster

Prob0, Prob1 = ThirdStep(pi0, pi1, M, pr_k_test, NormTestX, Size)

pyplot.imshow(pi0, cmap=pyplot.get_cmap('gray'))
pyplot.show()
pyplot.imshow(pi1, cmap=pyplot.get_cmap('gray'))
pyplot.show()

print("First claster: ")

sum0 = 0
for i in range(M):
    if (Prob0[i] > 0.5):
            sum0 = sum0 + 1
sum1 = M - sum0

fig, axes = pyplot.subplots(int(sum0/10) + 1, 10, figsize=(30, 30))
j = 0
k = 0
for i in range(M):
    if (Prob0[i] > 0.5):
        if (j == 10):
            j = 0
            k = k + 1
            axes[k, j].imshow(norm(testX[i]), cmap=pyplot.get_cmap('gray'))
            j = j + 1
        else:
            axes[k, j].imshow(norm(testX[i]), cmap=pyplot.get_cmap('gray'))
            j = j + 1
pyplot.show()

print("\nSecond claster: ")

fig, axes = pyplot.subplots(int(sum1/10) + 1, 10, figsize=(30, 30))
j = 0
k = 0
for i in range(M):
    if (Prob0[i] < 0.5):
        if (j == 10):
            j = 0
            k = k + 1
            axes[k, j].imshow(norm(testX[i]), cmap=pyplot.get_cmap('gray'))
            j = j + 1
        else:
            axes[k, j].imshow(norm(testX[i]), cmap=pyplot.get_cmap('gray'))
            j = j + 1
pyplot.show()
