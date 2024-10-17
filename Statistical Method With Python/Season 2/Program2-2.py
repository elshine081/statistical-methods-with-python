from numpy import random
import matplotlib.pyplot as plt
from statistics import variance

def lammbdahatPoison(_iteration, _sampleSize, _lambda):
    iter = _iteration
    n = _sampleSize
    iterBar = [0]*_iteration

    for i in range(0,iter):
        vPois = random.poisson(lam=_lambda,size=n)
        iterBar[i] = sum(vPois)/len(vPois)

    plt.hist(iterBar)
    plt.show()

    lambdaHat = sum(iterBar)/len(iterBar)
    varLambdaHat = variance(iterBar)

    return [lambdaHat, varLambdaHat]

result = lammbdahatPoison(1000,100,5)

print("lambda :",result[0],"\nlambda var :",result[1])