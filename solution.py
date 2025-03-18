import numpy as numpy
import pyrosim.pyrosim as pyrosim
import random as random
import os as os

class SOLUTION:
    def __init__(self):
        self.weights = numpy.array([[numpy.random.rand(), numpy.random.rand()], [numpy.random.rand(), numpy.random.rand()], [numpy.random.rand(), numpy.random.rand()]])
        self.weights = (self.weights * 2) - 1

    def evaluate(self, runType):
        self.create_mind()
        self.create_body()
        self.create_world()
        os.system("python simulate.py " + runType)
        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.read())

    def create_body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
        pyrosim.End()
    def create_mind(self):
        pyrosim.Start_NeuralNetwork("brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg")
        pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
        for currentRow in range(0, 3):
            for currentCol in range(3, 5):
                pyrosim.Send_Synapse(currentRow, currentCol, self.weights[currentRow][currentCol-3])
        pyrosim.End()
    def create_world(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-10, 10, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def mutate(self):
        rowToMut = random.randint(0, 2)
        colToMut = random.randint(0, 1)
        self.weights[rowToMut][colToMut] = random.random() * 2 - 1
