import numpy as numpy
import matplotlib.pyplot as plot

backLegSensorData = numpy.load("data/backleg.npy")
frontLegSensorData = numpy.load("data/frontleg.npy")

plot.plot(backLegSensorData, label="Back Leg Sensor Data", color="blue", linewidth="4")
plot.plot(frontLegSensorData, label="Front Leg Sensor Data", color="red", linewidth="1")
plot.show()
