from itertools import combinations_with_replacement

#Head & Tail:
def head(lst, num):
    return(lst[:num])

def tail(lst, num):
    return (lst[-num:])

data = [6,5,3,13,12,22,11]
data.sort()

combs = list(combinations_with_replacement(data[:5],4))
print(head(combs,8))
print(tail(combs,8))