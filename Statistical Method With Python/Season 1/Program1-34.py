import numpy

data = [1,3,5,4,2,12,42,51,75,86,15,2,5,2,54,61,51,24,21,45,1,2,5,24,5,4,55,4,1,55,44,22,33]

print(numpy.quantile(data,0.25))
print(numpy.quantile(data,0.5))
print(numpy.quantile(data,0.75))
print(numpy.quantile(data,0.37))
print(numpy.quantile(data,0.2))
print(numpy.quantile(data,0.6))