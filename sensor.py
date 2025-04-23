import numpy as numpy
import constants as c
import pyrosim.pyrosim as pyrosim
class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = numpy.zeros(c.STEPS)

    def get_value(self, timeStep):
        self.values[timeStep] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        #file.write(str(self.values[timeStep]) + '\n')
        #if timeStep == c.STEPS-1:
            #print(self.values)