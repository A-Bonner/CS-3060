from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import pyrosim.pyrosim as pyrosim
import time as t
import sys as sys
import os as os

class SIMULATION:

    def __init__(self):
        self.directOrGUI = sys.argv[1]
        self.brainID = sys.argv[2]
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif self.directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.GRAV)
        self.world = WORLD()
        self.robot = ROBOT(self.brainID)

    def run(self):
        file = open("tmp" + str(self.brainID) + ".txt", "w")
        sensFile = open("sensor" + str(self.brainID) + ".txt", "w")
        for i in range(c.STEPS):
            p.stepSimulation()
            self.robot.think()
            self.robot.sense(i, sensFile)
            self.robot.act()
            zPos = self.get_fitness()
            file.write(str(zPos)+"\n")
            #print(i)

            if self.directOrGUI == "GUI":
                t.sleep(c.SLEEPTIME)
        sensFile.close()
        file.close()
        os.rename("tmp" + str(self.brainID) + ".txt", "fitness" + str(self.brainID) + ".txt")

    def get_fitness(self):
        return self.robot.get_fitness()

    def __del__(self):
        p.disconnect()