d = list(range(1,29)) #1,2,3,...,28

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
              
         

mat = matrix(d,4,7,False)
for i in mat:
    print(i)