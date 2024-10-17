from itertools import product

#Head & Tail:
def head(lst, num):
    return(lst[:num])

def tail(lst, num):
    return (lst[-num:])

data = [6,5,3,13,12,22,11]
data.sort()

perm = [x for x in product(data[:4], repeat=4)]
print(head(perm,8))
print(tail(perm,8))