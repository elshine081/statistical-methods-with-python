import pandas #pandas library must be installed

name = ["Javad","Ghadir","Gholam","Hasan","Hosein","Reza"]
income = [1000,2600,1300,1850,3000,1500]

dataFrame = pandas.DataFrame([name,income],index=["name","income"])
#print(dataFrame)

entet = ["Football","BasketBall","Swim","Badminton","Tenis","Handball"]

dataFrame2 = pandas.DataFrame([name,entet],index=["name","entet"])
#print(dataFrame2)

mergedDataFrame = pandas.DataFrame.merge(dataFrame2,dataFrame,how="outer")
mergedDataFrame.index = ["income","entet","name"]

print(mergedDataFrame)