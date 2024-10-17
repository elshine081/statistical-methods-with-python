from scipy.stats import f
from statistics import variance

def CI_Sigma2xOverSigma2y(data1,data2,gamma):
    n = len(data1)
    m = len(data2)

    nu1 = n - 1
    nu2 = m - 1

    alpha = 1 - gamma

    s2x = variance(data1)
    s2y = variance(data2)

    a1 = (s2x/s2y)*(f.ppf(1-alpha/2,nu1,nu2))
    a2 = (s2x/s2y)*(1/f.ppf(alpha/2,nu1,nu2))

    print("σ^2 x / σ^2 y is in (",a1,",",a2,")")

x = [2.90,5.33,7.26,7.35,4.14,4.48,2.18,3.72,5.22,5.85]
y = [6.16,2.94,5.45,4.83,4.78,9.53,9.86,9.46,4.77,-0.46,1.89,5.91,1.17,5.42,4.85,10.56]

CI_Sigma2xOverSigma2y(x,y,0.95)