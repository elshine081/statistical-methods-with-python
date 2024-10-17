r1 = list(range(11,21)) # 11,12,...,20
r2 = list(range(21,31)) # 21, 22,...,30
r3 = list(range(31,41)) # 31, 32,...,40

def rbind(*rows):
    list = []
    for i in rows:
        list.append(i)
    return list

matrix = rbind(r1,r2,r3)
for i in matrix:
    print(i)

print (matrix[0][1]) # row 1 col 2