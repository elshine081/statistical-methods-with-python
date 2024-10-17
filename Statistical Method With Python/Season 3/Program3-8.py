from scipy.stats import chi2

qchisq = lambda alpha, v : chi2.ppf(1-alpha,v)
print(qchisq(0.05,15))