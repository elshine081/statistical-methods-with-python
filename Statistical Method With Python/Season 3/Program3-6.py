from scipy.stats import norm
import math

def CIPercent(percent,n,gamma):
    pp = percent
    alpha=1-gamma
    a1=pp-norm.ppf(1-alpha/2)*math.sqrt(pp*(1-pp)/n)
    a2=pp+norm.ppf(1-alpha/2)*math.sqrt(pp*(1-pp)/n)

    print("p is in (",a1,",",a2,")")

CIPercent(0.03,1000,0.95)