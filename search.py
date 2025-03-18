import os as os
from hillClimber import HILLCLIMBER

for i in range(0,2):
    hc = HILLCLIMBER()
    hc.evolve()
    hc.show_best()

