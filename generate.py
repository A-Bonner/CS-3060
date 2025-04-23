import pyrosim.pyrosim as pyrosim
import random as random

def create_body():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Torso", pos=[0, 0, 1], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_FrontUpper", parent="Torso", child="FrontUpper", type="revolute", position=[0, 0.5, 1])
    pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.End()

def create_brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg")
    pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")
    pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")
    for i in range(0,3):
        for j in range(3,5):
            pyrosim.Send_Synapse(i, j, random.uniform(-1, 1))
    pyrosim.End()

def create_world():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[-10, 10, 0.5], size=[1, 1, 1])
    pyrosim.End()

def run():
    create_body()
    create_brain()
    create_world()
