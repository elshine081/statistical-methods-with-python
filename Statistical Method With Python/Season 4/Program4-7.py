from scipy.stats import norm
from math import sqrt

def CI_PercentTwoPop(x,n,y,m,gamma):
    px = x/n
    py = y/m

    alpha = 1 - gamma

    a1 = px - py - norm.ppf(1-alpha/2) * (sqrt(px*(1-px)/n)+py*(1-py)/m)
    a2 = px - py + norm.ppf(1-alpha/2) * (sqrt(px*(1-px)/n)+py*(1-py)/m)

    print("px - py is in (",a1,",",a2,")")

CI_PercentTwoPop(100,1000,25,500,.95)