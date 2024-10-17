from scipy.stats import f
import matplotlib.pyplot as plt

def floatRange(start,end,step):
    lst = []
    x = start

    while x<end:
        lst.append(format(x,".2f"))
        x = x+step
    
    return lst

def FisherPlot(m,nu1,nu2):
    x = floatRange(0,5,5/(m-1))
    y = x.copy()
    for i in range(len(x)):
        y[i] = f.pdf(float(y[i]),nu1,nu2)
    
    plt.plot(x,y)
    
    plt.ylabel("")
    plt.xlabel("")

    plt.show()

list(map(FisherPlot,[500]*6,[1,2,5,10,25,50],[1,1,2,1,10,50]))