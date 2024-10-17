from numpy import random
from scipy.stats import binom
from statistics import variance
import matplotlib.pyplot as plt
import pandas as pand

def floatRange(start,end,step):
    lst = []
    x = start

    while x<end:
        lst.append(format(x,".2f"))
        x = x+step
    
    return lst

def MLEBernoli(probability,samplesize,iteration):
    n = samplesize
    prob = probability
    iter = iteration

    y = random.binomial(1,prob,n)

    vectorP = floatRange(.01,.99,.05)
    Lout = [0,len(vectorP)]

    def LnLikelihood(vectorp,y):
#        logBernoli = binom.pmf(y,1,vectorP)
        logBernoli = binom.pmf(y,vectorp,1)
        return sum(logBernoli)
    
    for i in range(0,len(vectorP)):
        Lout[i] = LnLikelihood(vectorP[i],y)
    
    iterMean=[]
    for i in range(0,iter):
        x = random.binomial(1,prob,n)
        iterMean.append(sum(x)/len(x))
    
    print("MLE of probability of success(P hat)=",sum(iterMean)/len(iterMean),"\nVariance of MLE for probability of success (P hat)=",variance(iterMean))

    plt.plot([vectorP,Lout],x="probability of success",y="logLikelihood")
    plt.show()

    data = {"v":vectorP,"l":Lout}
    df = pand.DataFrame(data)
    return df

MLEBernoli(0.3,50,1000)