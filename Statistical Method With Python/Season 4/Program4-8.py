from scipy.stats import norm
from math import sqrt

def CI_PercentTwoPopData(data1,dist1,data2,dist2,gamma,cutpoint):
    d1 = []
    d2 = []
    
    for i in range(len(data1)):
        if (dist1[i] == 1):
            d1.append(data1[i])
    
    for i in range(len(data2)):
        if (dist2[i] == 1):
            d2.append(data2[i])
    
    for x in range(len(d1)):
        if (d1[x] > cutpoint):
            d1[x] = 1
        else:
            d1[x] = 0
    
    for x in range(len(d2)):
        if (d2[x] > cutpoint):
            d2[x] = 1
        else:
            d2[x] = 0
    
    x = sum(d1)
    y = sum(d2)

    n = len(data1)
    m = len(data2)

    px = x/n
    py = y/m

    alpha = 1 - gamma

    a1 = px - py - norm.ppf(1-alpha/2) * (sqrt(px*(1-px)/n)+py*(1-py)/m)
    a2 = px - py + norm.ppf(1-alpha/2) * (sqrt(px*(1-px)/n)+py*(1-py)/m)

    print ("px - py is in (",a1,",",a2,")")

data1 = [33,22,23,34,22,28,33,24,29,30,27,26,26,33,32,34,32,22,31,27,34,25,33,34,21,23,31,28,24,35,21,32,32,26,29,30,31,24,37,25,34,33,26,24,19]
data2 = [32,35,38,39,31,33,37,34,34,31,31,39,31,31,29,33,34,36,40,31,35,36,29,29,32,32,39,37,39,33,29,34,35,28,33,32,34,39,28,31,39,39,36,33,30,35,30,31,38,32,35,39,33,33,33]

dist1 = [0,0,0,0,1,0,1,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,1,1,1,1,0,1]
dist2 = [0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0]

CI_PercentTwoPopData(data1,dist1,data2,dist2,.95,24)