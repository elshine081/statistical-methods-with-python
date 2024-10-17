c1 = list(range(11,21)) # 11, 12,...,20
c2 = list(range(21,31)) # 21, 22,...,30
c3 = list(range(31,41)) # 31, 32,...,40

def cbind(*columns):
    finalList = []
    for i in range(0,len(c1),1):
        lst = []
        for x in range(0,len(columns),1):
            lst.append(columns[x][i])
        finalList.append(lst)
    return finalList

matrix = cbind(c1,c2,c3)
for i in matrix:
    print(i)

print(matrix[0][1])