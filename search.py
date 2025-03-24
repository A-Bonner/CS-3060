import os as os
from parallelHillClimber import PARALLELHILLCLIMBER
import time as time


for i in range(0,1):
    phc = PARALLELHILLCLIMBER()
    phc.evolve()
    phc.show_best()
    time.sleep(0.1)

