from solutionB import SOLUTIONB
import constants as c
import copy as copy
import os as os
import numpy as numpy

class PARALLELHILLCLIMBERB:
    def __init__(self):
        os.system("del brainB*.nndf")
        os.system("del fitnessB*.txt")
        os.system("del sensorB*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        self.data = numpy.zeros((c.populationSize, c.numberOfGenerations))
        for i in range(c.populationSize):
            print(i)
            self.parents[i] = SOLUTIONB(self.nextAvailableID)
            self.nextAvailableID += 1

    def evolve(self):
        self.evaluate(self.parents)
        for currentGen in range(c.numberOfGenerations):
            self.evolve_For_One_Generation(currentGen)

    def evolve_For_One_Generation(self, gen):
        self.spawn()
        self.mutate()
        self.evaluate(self.children)
        self.print(gen)
        self.select()

    def spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def mutate(self):
        for i in range(len(self.children)):
            self.children[i].mutate()

    def select(self):
        for i in range(len(self.parents)):
            if self.parents[i].fitness < self.children[i].fitness:
                self.parents[i] = self.children[i]

    def print(self, gen):
        #print(len(self.parents))
        for i in range(len(self.children)):
            # print("parent", i, ":", self.parents[i].fitness, "child", j, ":", self.children[j].fitness)
            self.data[i][gen] = self.children[i].fitness
            # print('\n')


    def show_best(self):
        highest = 0
        highID = c.numberOfGenerations+1
        for i in range(len(self.parents)):
            if self.parents[i].fitness > highest:
                highest = self.parents[i].fitness
                highID = i
        self.parents[highID].start_Simulation("GUI")
        self.best = highest


    def evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].start_Simulation("DIRECT")
        for i in range(len(solutions)):
            solutions[i].wait_For_Simulation_To_End()