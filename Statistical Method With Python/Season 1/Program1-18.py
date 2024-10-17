from itertools import permutations

data = [6,5,3,13,12,22,11]
data.sort()

print(set(permutations(data[:4],4)))