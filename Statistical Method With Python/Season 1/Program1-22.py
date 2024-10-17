from itertools import combinations

data = [6,5,3,13,12,22,11]

combs = list(combinations(data,2))

#print(combs)

for x in range(len(combs)):
    print(1+x, ":", combs[x])