import numpy as np
from statistics import variance
import matplotlib.pyplot as plt

def GammaMME(iteration,sample_size,alpha,beta):
    iter = iteration
    n = sample_size
    bar1 = [0]*iter
    bar2 = [0]*iter

    alphatilda = []
    betatilda = []

    for i in range(0,iter):
        v_gamma = np.random.gamma(size=n,shape=alpha,scale=beta)
        bar1[i] = sum(v_gamma)/len(v_gamma)
        v_gammaPowerTwo = []
        for x in v_gamma:
            v_gammaPowerTwo.append(x**2)
        bar2[i] = sum(v_gammaPowerTwo)/len(v_gamma)

    for x in range(0,len(bar1)):
        alphatilda.append(bar1[x]**2/(bar2[x]-bar1[x]**2))
        betatilda.append((bar2[x]-bar1[x]**2)/bar1[x])

    mmeAlpha = sum(alphatilda)/len(alphatilda)
    mmeBeta = sum(betatilda)/len(betatilda)

    varAlpha = variance(alphatilda)
    varBeta = variance(betatilda)

    alphaW = np.ones_like(alphatilda)/len(alphatilda)
    plt.hist(alphatilda,weights=alphaW)
    plt.show()

    betaW = np.ones_like(betatilda)/len(betatilda)
    plt.hist(betatilda,weights=betaW)
    plt.show()

    return {"MME.alpha":mmeAlpha,"variance.Of.MME.alpha":varAlpha,"MME.beta":mmeBeta,"variance.Of.MME.beta":varBeta}

print(GammaMME(1000,100,.25,1/4.75))