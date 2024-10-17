from scipy.stats import t
from math import sqrt
from statistics import stdev

def CI2_Diff_Mu_UnkhnownSigma(data1,data2,gamma):
    alpha = 1 - gamma
    n=len(data1)
    m=len(data2)
    xbar = sum(data1)/len(data1)
    ybar = sum(data2)/len(data2)
    sx = stdev(data1)
    sy = stdev(data2)

    nu = (sx**2/n+sy**2/m)**2/(sx**4/(n**2*(n-1))+(sy**4/(m**2*(m-1))))


    a1 = xbar-ybar-t.ppf(1-alpha/2,nu)*sqrt(sx**2/n+sy**2/m)
    a2 = xbar-ybar+t.ppf(1-alpha/2,nu)*sqrt(sx**2/n+sy**2/m)

    print("μ x - μ y is in (",a1,",",a2,")")

data1 = [35.5,36,34,33.5,34,36,35.5,35.5,33.5,38,36,28,32,33.5,33.5,31,32,32,32,33.5]
data2 = [36.5,35,33.9,33.8,37,34,33.5,32.5,35.5,37,35.5,29,33,34.5,36.5,31.5,32.5,32.7,33.2,35.5]

CI2_Diff_Mu_UnkhnownSigma(data1,data2,.96)