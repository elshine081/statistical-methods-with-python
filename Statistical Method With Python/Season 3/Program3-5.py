from scipy.stats import binom
import matplotlib.pyplot as plt

def floatRange(start,end,step):
    lst = []
    x = start

    while x<end:
        lst.append(format(x,".2f"))
        x = x+step
    
    return lst

def binplot(n,p):
    x = binom.pmf(range(0,n),n,float(p))
    names=list(range(1,n+1))
    plt.bar(names,x)
    #plt.title("B(n,p) ,n=",n,",p=",p)
    plt.show()

ns = [15]*6
ps = [0.03]+floatRange(0.1,1,0.2)

x = list(map(binplot,ns,ps))