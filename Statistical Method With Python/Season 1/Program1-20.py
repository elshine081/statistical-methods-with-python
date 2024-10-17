from itertools import combinations

data = [6,5,3,13,12,22,11]
data.sort()

combs = list(combinations(data[:5],4))
print(combs)