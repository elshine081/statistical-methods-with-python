from scipy.stats import norm
import math

def CI_Mu_khnownSigma(xbar,n,sigma,gamma):
    alpha = 1-gamma
    a1=xbar-norm.ppf(1-alpha/2)*(sigma/math.sqrt(n))
    a2=xbar+norm.ppf(1-alpha/2)*(sigma/math.sqrt(n))
    print("μ is in","()",a1,",",a2,")")

CI_Mu_khnownSigma(25,100,5,.95)