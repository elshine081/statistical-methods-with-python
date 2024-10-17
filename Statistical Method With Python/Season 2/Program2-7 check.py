from numpy import random
import matplotlib.pyplot as plt
from statistics import variance
from scipy.stats import expon
import math
import pandas as pand

def floatRange(start,end,step):
    lst = []
    x = start

    while x<=end:
        lst.append(format(x,".2f"))
        x = x+step
    
    return lst

def MLEExponential(_lambda,sampleSize,itteration):
    n = sampleSize
    mlambda = _lambda
    itter = itteration

    y = random.exponential(scale=1/mlambda,size=n)
    vectorLambda = floatRange(6,11,0.12)
    for i in range(len(vectorLambda)):
        vectorLambda[i] = 1/float(vectorLambda[i])
    
    Lout = [0]*len(vectorLambda)

    def LnLikelihood(vL,Y):
        logexponentional = expon.pdf(1/vL,Y)
        for i in range(len(logexponentional)):
            print(logexponentional[i])
            if (logexponentional[i] > 0):
                
        return(sum(logexponentional))
    
    for i in range(len(vectorLambda)):
        Lout[i]=LnLikelihood(vectorLambda[i],y)
    
    itterMean = []
    for i in range(itter):
        x = random.exponential(scale=1/mlambda,size=n)
        itterMean.append(sum(x)/len(x))
    
    print("MLE of lambda = ",sum(itterMean)/len(itterMean),"\nVariance of mle for lambda = ",variance(itterMean))

    plt.plot(vectorLambda*100,Lout)
    plt.show()

MLEExponential(1/10,100,1000)