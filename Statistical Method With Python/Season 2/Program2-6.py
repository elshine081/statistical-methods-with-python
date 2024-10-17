from numpy import random
import matplotlib.pyplot as plt
from statistics import variance
from scipy.stats import poisson
import math
import pandas as pand

def floatRange(start,end,step):
    lst = []
    x = start

    while x<=end:
        lst.append(format(x,".1f"))
        x = x+step
    
    return lst

def MLEPoison(_lambda,_samplesize,_itteration):
    n = _samplesize
    Lambda = _lambda
    itter = _itteration
    y = random.poisson(Lambda,n)
    vectorLambda = floatRange(1,10,0.5)
    lout = [0]*len(vectorLambda)

    def LnLikelihood(vLambda,Y):
        logPois = poisson.pmf(Y,float(vLambda))
        print("Y:",Y,"  lambda:",vLambda,"logPois:",logPois)
        return sum(logPois)
    
    for i in range(0,len(vectorLambda)):
        lout[i] = LnLikelihood(vectorLambda[i],y)
    
    itterMean = [0]*itter
    for i in range(0,itter):
        x = random.poisson(Lambda,n)
        itterMean[i] = sum(x)/len(x)
    
    print("MLE of lambda (lambda hat)=",sum(itterMean)/len(itterMean),"\nVariance of MLE for lambda (Lambda hat)=",variance(itterMean))

    #Plot

    data = {"v":vectorLambda,"l":lout}
    df = pand.DataFrame(data)
    return(df)

print(MLEPoison(3,100,1000))