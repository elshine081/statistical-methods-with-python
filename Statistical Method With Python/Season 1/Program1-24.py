from itertools import combinations
from statistics import variance

def comb_var(_comb):
    varList = []
    for x in _comb:
        varList.append(variance(x))
    return(varList)


data = [6,5,3,13,12,22,11]

combs = list(combinations(data,2))
combVar = comb_var(combs)

#print(combVar)

for i in range(len(combVar)):
    print(i+1, ":", combVar[i])