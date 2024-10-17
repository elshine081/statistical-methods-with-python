import random

random.seed(101)

def matrix(data,nrow,ncol,byrow):
    finalList = []
    
    if (byrow):
        for i in range(nrow):
                lst = []
                for x in range(ncol*i,(ncol*i)+ncol):
                    if (x >= len(d)):
                        break
                    lst.append(d[x])
                finalList.append(lst)
    else:
         for i in range(nrow):
              lst = []
              for x in range(ncol):
                   if (nrow*x+i >= len(d)):
                        break
                   lst.append(d[nrow*x+i])
              finalList.append(lst)
    
    return finalList

def CLTBinom(n,p,itter):
    for j in range(len(n)):
        M = 