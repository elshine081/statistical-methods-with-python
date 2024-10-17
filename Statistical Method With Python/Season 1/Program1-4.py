data = input("enter data : ").split() #Separate With Space (" ") example : 120 26 80 182 90

print("Data :",data)

data.sort(reverse=True)

print("Sorted Data (Reversed) :",data)

print(type(data)) #data type
print(type(data[0])) #data item type2