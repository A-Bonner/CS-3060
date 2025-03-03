from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.prepare_to_sense()
        self.prepare_to_act()

    def prepare_to_sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def sense(self, timeStep):
        for sen in self.sensors:
            self.sensors[sen].get_value(timeStep)

    def prepare_to_act(self):
        self.motors = {}
        self.amplitude = c.PI4THS
        self.frequency = c.FREQ
        self.offset = c.PHOFF
        for jointName in pyrosim.jointNamesToIndices:
            if jointName == "Torso_FrontLeg":
                self.motors[jointName] = MOTOR(jointName, self.amplitude)
            else:
                self.motors[jointName] = MOTOR(jointName, (self.amplitude * 2))



    def act(self, timeStep):
        for mot in self.motors:
            self.motors[mot].set_value(self.robotId, timeStep)