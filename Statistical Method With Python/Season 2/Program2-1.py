import numpy as nump
from statistics import variance
import matplotlib.pyplot as plt

#numpy and matplotlib must be installed

def phat_Bernoli(_iteration,_sampleSize,_probability):
    iter = _iteration
    n = _sampleSize
    p = _probability
    iterBar = [0]*iter

    for x in range(0,iter):
        v_Bernoli = nump.random.binomial(1,p,n)
        iterBar[x]=sum(v_Bernoli)/len(v_Bernoli)
    
    plt.hist(iterBar)
    plt.show()

    phat=sum(iterBar)/len(iterBar)
    var_phat = variance(iterBar)

    return [phat,var_phat]

result=phat_Bernoli(1000,100,0.3)

print("phat :",result[0],"\nphat variance :",result[1])