#sequence
def sequence(_from,_to,lngtout):
    i=_from
    step = _to/(lngtout-1)
    lst = []

    while i<_to:
        lst.append(round(i,8))
        i+=step
    
    lst[-1]=_to
    
    return lst

x=sequence(0,1,20)

#print(x)

for i in x:
    print(x.index(i)+1 , ":", i)

#seq
def seq(_from,_to,_step):
    i=_from
    lst = []

    while i<_to:
        lst.append(i)
        i+=_step

    return lst

y=seq(10,20,0.75)

#print(y)

for i in y:
    print(y.index(i)+1 , ":", i)