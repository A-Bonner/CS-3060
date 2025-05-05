import numpy as numpy
import matplotlib.pyplot as plot
import constants as c

aFitnessData = numpy.load("AFitnesses.npy")
bFitnessData = numpy.load("BFitnesses.npy")
aMeans = []
bMeans = []
for i in range(0, c.numberOfGenerations):
  aMeans.append(numpy.mean(aFitnessData, axis=0))
  bMeans.append(numpy.mean(aFitnessData, axis=0))

  plot.plot(aFitnessData, label="A", color="blue", linewidth="4")
  plot.plot(bFitnessData, label="B", color="red", linewidth="2")
  plot.savefig("ABtest")


