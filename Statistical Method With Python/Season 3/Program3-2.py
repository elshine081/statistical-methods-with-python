from scipy.stats import norm
import math

def CI2_Mu_khnownSigma(data,sigma,gamma):
    alpha = 1-gamma
    xbar = sum(data)/len(data)
    n = len(data)
    a1=xbar-norm.ppf(1-alpha/2)*(sigma/math.sqrt(n))
    a2=xbar+norm.ppf(1-alpha/2)*(sigma/math.sqrt(n))
    print("μ is in","()",a1,",",a2,")")

data = [35,36,34,33,34,36,35,35,33,38,36,28,32,33,33,32,31,32,32,33]

CI2_Mu_khnownSigma(data,2,.90)