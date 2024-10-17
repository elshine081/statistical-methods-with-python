from scipy.stats import chi2
import matplotlib.pyplot as plt

def floatRange(start,end,step):
    lst = []
    x = start

    while x<end:
        lst.append(format(x,".6f"))
        x = x+step
    
    return lst

def chisqPlot(m,nu):
    x = floatRange(0,50,50/m)
    y = []
    for z in x:
        y.append(chi2.pdf(float(z),nu))

    plt.plot(x,y)
    plt.xlabel("")
    plt.ylabel("")
    plt.title(f"Chi-Squared(n), n={nu}")
    plt.show()

nus = list(range(5,35,5))
ms = [500]*len(nus)
x = list(map(chisqPlot,ms,nus))