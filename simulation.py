from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import pyrosim.pyrosim as pyrosim
import time as t
import sys as sys

class SIMULATION:

    def __init__(self):
        self.directOrGUI = sys.argv[1]
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif self.directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.GRAV)
        self.world = WORLD()
        self.robot = ROBOT()

    def run(self):
        for i in range(c.STEPS):
            p.stepSimulation()
            self.robot.think()
            self.robot.sense(i)
            self.robot.act()
            #print(i)

            t.sleep(c.SLEEPTIME)

    def get_fitness(self):
        self.robot.get_fitness()

    def __del__(self):
        p.disconnect()