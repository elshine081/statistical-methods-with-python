from itertools import permutations # install package and library ...

numbers = [7,10,3,11,17,22,36]

#print all 3 permutations
for x in list(permutations(numbers,3)):
    print(x)

#only 3 permutations with 3
for i in list(permutations(numbers,3)):
    if 3 in i:
        print(i)