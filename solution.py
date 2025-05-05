import numpy as numpy
import pyrosim.pyrosim as pyrosim
import random as random
import os as os
import time as time
import constants as c

class SOLUTION:
    def __init__(self, ID):
        self.myID = ID
        self.weights = numpy.zeros((c.numSensorNeurons, c.numMotorNeurons))
        for i in range(c.numSensorNeurons):
            for j in range(c.numMotorNeurons):
                self.weights[i][j] = (numpy.random.rand() * 2) -1
                #print(self.weights[i][j])

    def evaluate(self, runType):
        self.start_Simulation(runType)
        self.wait_For_Simulation_To_End()

    def start_Simulation(self, runType):
        self.create_mind()
        self.create_body()
        self.create_world()
        os.system("start /B python simulate.py " + runType + " " + str(self.myID))

    def wait_For_Simulation_To_End(self):
        while not os.path.exists("fitnessA" + str(self.myID) + ".txt"):
            time.sleep(0.2)
        try:
            with open("fitnessA" + str(self.myID) + ".txt", "r") as fitnessFile:
                positions = fitnessFile.readlines()
                maxHeight = 0
                for line in positions:
                    height = float(line)
                    if height > maxHeight:
                        maxHeight = height
                self.fitness = maxHeight
            with open("sensorA" + str(self.myID) + ".txt", "r") as sensorFile:
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
        os.system("del fitnessA" + str(self.myID) + ".txt")
        os.system("del sensorA" + str(self.myID) + ".txt")
        print(self.fitness, '\n')

    def create_body(self):
        pyrosim.Start_URDF("bodyA.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])

        pyrosim.Send_Joint(name="Torso_FrontUpper", parent="Torso", child="FrontUpper", type="revolute", position=[0, 0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="FrontUpper", pos=[0, 0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="FrontUpper_FrontLower", parent="FrontUpper", child="FrontLower", type="revolute", position=[0, 1, 0], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="FrontLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_BackUpper", parent="Torso", child="BackUpper", type="revolute", position=[0, -0.5, 1], jointAxis="1 0 0")
        pyrosim.Send_Cube(name="BackUpper", pos=[0, -0.5, 0], size=[0.2,1,0.2])
        pyrosim.Send_Joint(name="BackUpper_BackLower", parent="BackUpper", child="BackLower", type="revolute", position=[0, -1, 0], jointAxis="0 0 1")
        pyrosim.Send_Cube(name="BackLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_LeftUpper", parent="Torso", child="LeftUpper", type="revolute", position=[0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftUpper", pos=[0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="LeftUpper_LeftLower", parent="LeftUpper", child="LeftLower", type="revolute", position=[1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="LeftLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

        pyrosim.Send_Joint(name="Torso_RightUpper", parent="Torso", child="RightUpper", type="revolute", position=[-0.5, 0, 1], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightUpper", pos=[-0.5, 0, 0], size=[1, 0.2, 0.2])
        pyrosim.Send_Joint(name="RightUpper_RightLower", parent="RightUpper", child="RightLower", type="revolute", position=[-1, 0, 0], jointAxis="0 1 0")
        pyrosim.Send_Cube(name="RightLower", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])
        pyrosim.End()

    def create_mind(self):
        pyrosim.Start_NeuralNetwork("brainA" + str(self.myID) + ".nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontUpper")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLower")
        pyrosim.Send_Sensor_Neuron(name=3, linkName="BackUpper")
        pyrosim.Send_Sensor_Neuron(name=4, linkName="BackLower")
        pyrosim.Send_Sensor_Neuron(name=5, linkName="LeftUpper")
        pyrosim.Send_Sensor_Neuron(name=6, linkName="LeftLower")
        pyrosim.Send_Sensor_Neuron(name=7, linkName="RightUpper")
        pyrosim.Send_Sensor_Neuron(name=8, linkName="RightLower")

        pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_FrontUpper")
        pyrosim.Send_Motor_Neuron(name=10, jointName="FrontUpper_FrontLower")
        pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_BackUpper")
        pyrosim.Send_Motor_Neuron(name=12, jointName="BackUpper_BackLower")
        pyrosim.Send_Motor_Neuron(name=13, jointName="Torso_LeftUpper")
        pyrosim.Send_Motor_Neuron(name=14, jointName="LeftUpper_LeftLower")
        pyrosim.Send_Motor_Neuron(name=15, jointName="Torso_RightUpper")
        pyrosim.Send_Motor_Neuron(name=16, jointName="RightUpper_RightLower")

        for currentRow in range(c.numSensorNeurons):
            for currentCol in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(currentRow, currentCol+c.numSensorNeurons, self.weights[currentRow][currentCol])
        pyrosim.End()
    def create_world(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-10, 10, 0.5], size=[1, 1, 1])
        pyrosim.End()

    def mutate(self):
        rowToMut = random.randint(0, (c.numSensorNeurons-1))
        colToMut = random.randint(0, (c.numMotorNeurons-1))
        self.weights[rowToMut][colToMut] = (numpy.random.rand() * 2) - 1

    def set_ID(self, ID):
        self.myID = ID
