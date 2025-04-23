import random
import constants as c
import numpy as numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim
class MOTOR:

    def __init__(self, jointName, amp):
        self.jointName = jointName
        self.amplitude = amp
        self.frequency = c.FREQ
        self.phaseOffset = c.PHOFF
        self.targetStart = [random.uniform(-c.PI4THS, 0) for i in range(c.STEPS)]
        self.values = [self.amplitude * numpy.sin(self.frequency * i + self.phaseOffset) for i in self.targetStart]

    def set_value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = c.NEWTONS)
