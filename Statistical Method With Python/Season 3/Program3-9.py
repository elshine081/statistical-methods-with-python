from scipy.stats import chi2
import math

qchisq = lambda a, v : chi2.ppf(a,v)

def CI_Sigma2(n,s,gamma):
    nu=n-1
    alpha=1-gamma
    s2=s**2
    a1=s2*(nu)/qchisq(1-alpha/2,nu)
    a2=s2*(nu)/qchisq(alpha/2,nu)

    print("σ^2 is in (",a1,",",a2,")")

CI_Sigma2(31,math.sqrt(1.5),0.95)