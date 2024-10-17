def gl(rng,rpt):
    lst = []
    for i in range(rng):
        for x in range(rpt):
            lst.append(i+1)
    return lst

x = gl(5,3)
print(x)
print("Levels:",list(set(x)))