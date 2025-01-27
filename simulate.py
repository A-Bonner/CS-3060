import pybullet as p
import time as t

physicsClient = p.connect(p.GUI)

for i in range(100000):
    p.stepSimulation()
    t.sleep((1/120))
    print(i)

p.disconnect()