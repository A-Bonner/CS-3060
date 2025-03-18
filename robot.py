from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
class ROBOT:

    def __init__(self):

        self.robotId = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
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



    def act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].set_value(self.robotId, desiredAngle)

    def think(self):
        self.nn.Update()

    def get_fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId, 0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        file = open("fitness.txt", "w")
        file.write(str(xCoordinateOfLinkZero))
        exit()
