import numpy as numpy
import pyrosim.pyrosim as pyrosim
import random as random
import os as os
import time as time
import constants as c

class SOLUTIONB:
    def __init__(self, ID):
        self.myID = ID
        self.weights = numpy.zeros((c.numSensorNeurons, c.numMotorNeurons))
        for i in range(c.numSensorNeurons):
            for j in range(c.numMotorNeurons):
                self.weights[i][j] = (numpy.random.rand() * 2) -1
                print(self.weights[i][j])

    def evaluate(self, runType):
        self.start_Simulation(runType)
        self.wait_For_Simulation_To_End()

    def start_Simulation(self, runType):
        self.create_mind()
        self.create_body()
        self.create_world()
        os.system("start /B python simulateB.py " + runType + " " + str(self.myID))

    def wait_For_Simulation_To_End(self):
        while not os.path.exists("fitnessB" + str(self.myID) + ".txt"):
            time.sleep(0.2)
        try:
            with open("fitnessB" + str(self.myID) + ".txt", "r") as fitnessFile:
                positions = fitnessFile.readlines()
                maxHeight = 0
                for line in positions:
                    height = float(line)
                    if height > maxHeight:
                        maxHeight = height
                self.fitness = maxHeight
            with open("sensorB" + str(self.myID) + ".txt", "r") as sensorFile:
                hop = False
                jumpLen = 0
                maxJump = 0
                sensorData = sensorFile.readlines()
                for line in sensorData:
                    if "-1.0" not in line:
                        hop = True
                        jumpLen += 1
                    else:
                        if jumpLen > maxJump:
                            maxJump = jumpLen
                        jumpLen = 0
                if not hop:
                    self.fitness -= 5
                else:
                    self.fitness += (100 * (maxJump/len(sensorData)))

        except PermissionError:
            time.sleep(0.2)
        #fitnessFile.close()
        os.system("del fitnessB" + str(self.myID) + ".txt")
        os.system("del sensorB" + str(self.myID) + ".txt")

    def create_body(self):
        pyrosim.Start_URDF("bodyB.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 2, 1])

        pyrosim.Send_Joint(name="Torso_FrontRightUpper", parent="Torso", child="FrontRightUpper", type="revolute", position=[0.5, 0.75, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontRightUpper", pos=[0.5, 0, 0], size=[1,0.2,0.2])
        pyrosim.Send_Joint(name="FrontRightUpper_FrontRightLower", parent="FrontRightUpper", child="FrontRightLower", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontRightLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_BackRightUpper", parent="Torso", child="BackRightUpper", type="revolute", position=[0.5, -0.75, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackRightUpper", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="BackRightUpper_BackRightLower", parent="BackRightUpper", child="BackRightLower", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackRightLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_BackLeftUpper", parent="Torso", child="BackLeftUpper", type="revolute", position=[-0.5, -0.75, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="BackLeftUpper", pos=[-0.5, 0, 0], size=[1,0.2,0.2])
        pyrosim.Send_Joint(name="BackLeftUpper_BackLeftLower", parent="BackLeftUpper", child="BackLeftLower", type="revolute", position=[-1, 0, 0], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="BackLeftLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_FrontLeftUpper", parent="Torso", child="FrontLeftUpper", type="revolute", position=[-0.5, 0.75, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeftUpper", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="FrontLeftUpper_FrontLeftLower", parent="FrontLeftUpper", child="FrontLeftLower", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="FrontLeftLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.End()

    def create_mind(self):
        pyrosim.Start_NeuralNetwork("brainB" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontRightUpper")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontRightLower")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="BackLeftUpper")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="BackLeftLower")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="FrontLeftUpper")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="FrontLeftLower")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="BackRightUpper")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="BackRightLower")

        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_FrontRightUpper")
        pyrosim.Send_Motor_Neuron(name=10, jointName="FrontRightUpper_FrontRightLower")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_BackLeftUpper")
        pyrosim.Send_Motor_Neuron(name=12, jointName="BackLeftUpper_BackLeftLower")
        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_FrontLeftUpper")
        pyrosim.Send_Motor_Neuron(name=14, jointName="FrontLeftUpper_FrontLeftLower")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_BackRightUpper")
        pyrosim.Send_Motor_Neuron(name=16, jointName="BackRightUpper_BackRightLower")

        for currentRow in range(c.numSensorNeurons):
            for currentCol in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(currentRow, currentCol+c.numSensorNeurons, self.weights[currentRow][currentCol])
        pyrosim.End()
    def create_world(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-10, 10, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def mutate(self):
        rowToMut = random.randint(0, (c.numSensorNeurons - 1))
        colToMut = random.randint(0, (c.numMotorNeurons - 1))
        self.weights[rowToMut][colToMut] = (numpy.random.rand() * 2) - 1

    def set_ID(self, ID):
        self.myID = ID
