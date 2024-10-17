A = [2,4,4,7,3,2,6,3,4,1]
B = [3,7,3,4,4,7]

# first method : convert list to set and use & and |
print ("intersect : ", set(A)&set(B))
print ("union : ", set(A)|set(B))

# second method : manual for loop
intersectList = []
for x in A:
    if x in B:
        intersectList.append(x)

intersectList = list(set(intersectList)) #delete duplicates (set doesnt contain duplicate items) : cast to set then cast to list again

print("intersect :", intersectList)

unionList = A + B
unionList = list(set(unionList)) #delete duplicates

print("union : ", unionList)