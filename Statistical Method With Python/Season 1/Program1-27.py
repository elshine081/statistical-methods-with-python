def sequence(*nums):
    list = []
    for x in nums:
        for i in range(x):
            list.append(i+1)
    return list

print(sequence(7,8))