import numpy

data = numpy.genfromtxt(fname="housing.data")

for line in data:
    print(*line)
