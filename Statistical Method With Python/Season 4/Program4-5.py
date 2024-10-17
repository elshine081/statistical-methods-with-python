from scipy.stats import t
from math import sqrt

def CI1_Diff_Mu_UnkhnownSigmaPooled(n,xbar,sx,m,ybar,sy,gamma):
    alpha = 1-gamma
    nu = n+m-2

    sp = sqrt(((n-1)*sx**2+(m-1)*sy**2)/nu)

    a1 = xbar-ybar-t.ppf(1-alpha/2,nu)*sp*sqrt(1/n+1/m)
    a2 = xbar-ybar+t.ppf(1-alpha/2,nu)*sp*sqrt(1/n+1/m)

    print("μ x - μ y is in (",a1,",",a2,")")

CI1_Diff_Mu_UnkhnownSigmaPooled(20,200,sqrt(100),30,350,sqrt(150),.95)