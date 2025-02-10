import pybullet as p
import pybullet_data
import time as t
from generate import *

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

create_world()
create_robot()

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
for i in range(100000):
    p.stepSimulation()
    t.sleep((1/120))
    print(i)

p.disconnect()