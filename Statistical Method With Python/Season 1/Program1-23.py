from itertools import combinations

def comb_mean(_comb):
    meanList = []
    for x in _comb:
        meanList.append(sum(x)/len(x))
    return meanList

data = [6,5,3,13,12,22,11]

combs = list(combinations(data,2))
combMean = comb_mean(combs)

#print(combMean)

for x in range(len(combMean)):
    print(1+x, ":", combMean[x])