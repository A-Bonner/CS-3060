from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import constants as c
import pyrosim.pyrosim as pyrosim
import time as t

class SIMULATION:

    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, c.GRAV)
        self.world = WORLD()
        self.robot = ROBOT()

    def run(self):
        for i in range(c.STEPS):
            p.stepSimulation()
            self.robot.sense(i)
            self.robot.act(i)
            print(i)

            t.sleep(c.SLEEPTIME)

    def __del__(self):
        p.disconnect()