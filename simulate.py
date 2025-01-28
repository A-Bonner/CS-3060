import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")
for i in range(100000):
    p.stepSimulation()
    t.sleep((1/120))
    print(i)

p.disconnect()