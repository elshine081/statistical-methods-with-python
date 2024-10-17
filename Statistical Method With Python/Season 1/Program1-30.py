import pandas #pandas library must be installed

data = {"x":[1]*10,"y":[10,20]*5,"z":list(range(1,11))} #this is a dictionary
dataFrame = pandas.DataFrame(data, index=list(range(1,11))) #data frame

filteredDataFrame = None
lst = []

for i in range(1,11):
    if (dataFrame.loc[i]["y"]==20):
        lst.append(dataFrame.loc[i])

filteredDataFrame = pandas.DataFrame(lst)

print(filteredDataFrame)