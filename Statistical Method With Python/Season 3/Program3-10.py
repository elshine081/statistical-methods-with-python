from scipy.stats import chi2
import math
from statistics import variance

qchisq = lambda a, v : chi2.ppf(a,v)

def CI_Sigma2_Data(data,gamma):
    nu=len(data)-1
    alpha=1-gamma
    s2=variance(data)
    a1=s2*(nu)/qchisq(1-alpha/2,nu)
    a2=s2*(nu)/qchisq(alpha/2,nu)
    a1s=math.sqrt(a1)
    a2s=math.sqrt(a2)
    print("σ^2 is in (",a1,",",a2,")\nσ is in (",a1s,",",a2s,")")

data = [296,279,302,301.5,311,315,297,298,299,305,306,317,302,301,353,340,337,317,319,320,321]
CI_Sigma2_Data(data,0.90)