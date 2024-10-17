from statistics import variance

d = [14,15,16,25,14,12,26,32,17,11,12,14]

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

def rowSum(_matrix):
     sumList = []
     for i in _matrix:
          sumList.append(sum(i))
     return sumList

mat = matrix(d,3,4,True)
for i in mat:
    print(i)

print(rowSum(mat))