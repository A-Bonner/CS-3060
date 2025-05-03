import os as os
from parallelHillClimber import PARALLELHILLCLIMBER
from parallelHillClimberB import PARALLELHILLCLIMBERB
import time as time
import numpy as numpy

#for i in range(0,1):
phcA = PARALLELHILLCLIMBER()
phcA.evolve()
time.sleep(0.1)
numpy.save("AFitnesses.npy", phcA.data)

time.sleep(2)

phcB = PARALLELHILLCLIMBERB()
phcB.evolve()
time.sleep(0.1)
numpy.save("BFitnesses.npy", phcB.data)

phcA.show_best()
phcB.show_best()
