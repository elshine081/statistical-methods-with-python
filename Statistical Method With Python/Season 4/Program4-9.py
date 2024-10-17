from scipy.stats import t
from math import sqrt
from statistics import stdev

def CI_Mu_pair(data1,data2,gamma):
    n = len(data1)
    diff = []
    for i in range(len(data1)):
        diff.append(data1[i] - data2[i])
    
    diffMean = sum(diff)/len(diff)
    a1 = diffMean - t.ppf(gamma,n-1)*stdev(diff)/sqrt(n)
    a2 = diffMean + t.ppf(gamma,n-1)*stdev(diff)/sqrt(n)

    print("μ d is in (",a1,",",a2,")")

data1 = [78,74,76,81,82,78,73,70,78,79,83,81,73,71,75]
data2 = [73,73,76,80,80,76,72,71,73,81,77,80,70,68,73]

CI_Mu_pair(data1,data2,.95)