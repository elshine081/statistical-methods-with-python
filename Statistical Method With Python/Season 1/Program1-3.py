import math

data = [15,11,13,10,9,16,14,14,11,13,12,14,12,11,15,11,15,11,13,14,14,9,14,11,15]

def listSquareRoot(_lst):
    _finList = []
    for i in _lst:
        _finList.append(math.sqrt(i))
    return _finList

def listRound(_lst,_digit):
    _finList = []
    for i in _lst:
        _finList.append(round(i,_digit))
    return _finList

print(listRound(listSquareRoot(data),3))

#Head & Tail:
def head(lst, num):
    return(lst[:num])

def tail(lst, num):
    return (lst[-num:])

print(head(data,3)) #Print Last 3 Items Of Data
print(tail(data,3)) #Print First 3 Items Of Data

#Sort List
sorted_data = data.copy() #clone
sorted_data.sort(reverse=False) #reverse = decreasing
print(sorted_data)

reverse_sorted_data = data.copy()
reverse_sorted_data.sort(reverse=True)
print(reverse_sorted_data)

#Mode
print(type(data)) #type of data is a list.