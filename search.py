import os as os
from parallelHillClimber import PARALLELHILLCLIMBER
from parallelHillClimberB import PARALLELHILLCLIMBERB
import time as time
import numpy as numpy

bestFileA = open("BestFitnessesA.txt", "w")
bestFileB = open("BestFitnessesB.txt", "w")
for i in range(0,10):
    phcA = PARALLELHILLCLIMBER()
    phcA.evolve()
    time.sleep(0.1)
    numpy.save("AFitnesses"+str(i)+".npy", phcA.data)
    phcA.show_best()
    bestFileA.write(str(phcA.best)+'\n')

    time.sleep(2)

    phcB = PARALLELHILLCLIMBERB()
    phcB.evolve()
    time.sleep(0.1)
    numpy.save("BFitnesses"+str(i)+".npy", phcB.data)
    phcB.show_best()
    bestFileB.write(str(phcB.best) + '\n')

    time.sleep(2)
bestFileA.close()
bestFileB.close()
