import numpy

data = numpy.genfromtxt(fname="housing.data")

################# Advanced
for line in data:
    print(*line)

################# Reach 1
for line in data:
    list = line.tolist()
    strList = [str(i) for i in list]
    print(strList)

