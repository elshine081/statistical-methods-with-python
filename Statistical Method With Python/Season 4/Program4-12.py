from scipy.stats import f

def CI_Sigma2xOverSigma2y(n,m,sx,sy,gamma):
    nu1 = n - 1
    nu2 = m - 1

    alpha = 1 - gamma

    s2x = sx**2
    s2y = sy**2

    a1 = (s2x/s2y)*(f.ppf(1-alpha/2,nu1,nu2))
    a2 = (s2x/s2y)*(1/f.ppf(alpha/2,nu1,nu2))

    print("σ^2 x / σ^2 y is in (",a1,",",a2,")")

CI_Sigma2xOverSigma2y(8,9,5,7,0.90)