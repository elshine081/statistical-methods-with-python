from scipy.stats import t
import math
from statistics import stdev

def CI_Mu_UnkhnownSigma(data,gamma):
    xbar = sum(data)/len(data)
    n=len(data)
    nu=n-1
    alpha=1-gamma
    s=stdev(data)
    a1=xbar-t.ppf(1-alpha/2,nu)*(s/math.sqrt(n))
    a2=xbar+t.ppf(1-alpha/2,nu)*(s/math.sqrt(n))
    print("μ is in","()",a1,",",a2,")")

data = [11,12,16.5,17,14,13.5,14.5,13,8,9,16,16.5,17,17.5,14,13,17,16,15,12]

CI_Mu_UnkhnownSigma(data,0.94)