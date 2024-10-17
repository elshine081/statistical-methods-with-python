from scipy.stats import t
from math import sqrt

def CI1_Diff_Mu_UnkhnownSigma(n,xbar,sx,m,ybar,sy,gamma):
    alpha = 1 - gamma
    nu = (sx**2/n+sy**2/m)**2/(sx**4/(n**2*(n-1))+(sy**4/(m**2*(m-1))))
    a1 = xbar-ybar-t.ppf(1-alpha/2,nu)*sqrt(sx**2/n+sy**2/m)
    a2 = xbar-ybar+t.ppf(1-alpha/2,nu)*sqrt(sx**2/n+sy**2/m)

    print("μ x - μ y is in (",a1,",",a2,")")

CI1_Diff_Mu_UnkhnownSigma(20,200,sqrt(100),30,350,sqrt(150),0.95)