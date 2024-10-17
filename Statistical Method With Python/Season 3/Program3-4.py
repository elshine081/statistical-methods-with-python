from scipy.stats import norm
from scipy.stats import t
import matplotlib.pyplot as plt

def floatRange(start,end,step):
    lst = []
    x = start

    while x<end:
        lst.append(format(x,".2f"))
        x = x+step
    
    return lst

x = floatRange(-5,5,1/50) #1/50 = (5-(-5))/500
z=[]
for i in x:
    z.append(norm.pdf(float(i)))
nu=[1,2,3,5,10,25]
mm=1.5

for i in range(0,len(nu)):
    y = []
    for q in x:
        y.append(t.pdf(float(q),nu[i]))

    plt.plot(x,z)
    plt.plot(x,y,color="blue")

    plt.xlabel("")
    plt.ylabel("")

    axis = plt.gca()
    axis.get_yaxis().set_visible(False)
    axis.get_xaxis().set_visible(False)

    #Legend Options Here

    plt.show()