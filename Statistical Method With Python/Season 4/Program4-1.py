from scipy.stats import norm
from math import sqrt

def CI_Diff_Mu_khnownSigma(n,xbar,sigmax,m,ybar,sigmay,gamma):
    alpha=1-gamma
    a1=xbar-ybar-norm.ppf(1-alpha/2)*sqrt(sigmax**2/n+sigmay**2/m)
    a2=xbar-ybar+norm.ppf(1-alpha/2)*sqrt(sigmax**2/n+sigmay**2/m)
    print("μ x - μ y is in (",a1,",",a2,")")

CI_Diff_Mu_khnownSigma(8,22.5,1.4,12,27,1.7,0.95)