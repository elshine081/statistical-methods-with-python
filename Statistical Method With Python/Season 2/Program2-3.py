from numpy import random
import matplotlib.pyplot as plt
from statistics import variance

def lammbdahatExponential(_iteration, _sampleSize, _lambda):
    iter = _iteration
    n = _sampleSize
    theta=1/_lambda
    iterBar = [0]*iter

    for i in range(0,iter):
        vExp = random.exponential(theta,n)
        iterBar[i] = sum(vExp)/len(vExp)

    plt.hist(iterBar)
    plt.show()

    lambdaHat = sum(iterBar)/len(iterBar)
    varLambdaHat = variance(iterBar)

    return [lambdaHat, varLambdaHat]

result = lammbdahatExponential(1000,100,10)

print("lambdahat :",result[0],"\nlambda var :",result[1])