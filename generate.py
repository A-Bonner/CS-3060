import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = -2.5
y = -2.5
z = 0.5
for i in range (0,5):
    for j in range (0,5):
        for k in range(0,10):
            pyrosim.Send_Cube(name="Box"+str(i), pos=[x, y, z], size=[length, width, height])
            bottom = z + (height/2)
            length = length * 0.9
            width = width * 0.9
            height = height * 0.9
            midpoint = height/2
            z = bottom + midpoint
        z = 0.5
        x = x + 1
        length = 1
        width = 1
        height = 1
    x = -2.5
    y = y + 1

pyrosim.End()
