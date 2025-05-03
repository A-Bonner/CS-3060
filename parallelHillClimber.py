from solution import SOLUTION
import constants as c
import copy as copy
import os as os
import numpy as numpy

class PARALLELHILLCLIMBER:
    def __init__(self):
        os.system("del brainA*.nndf")
        os.system("del fitnessA*.txt")
        os.system("del sensorA*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        self.data = numpy.zeros((c.populationSize, c.numberOfGenerations))
        for i in range(c.populationSize):
            print(i)
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def evolve(self):
        self.evaluate(self.parents)
        for currentGen in range(c.numberOfGenerations):
            self.evolve_For_One_Generation()

    def evolve_For_One_Generation(self):
        self.spawn()
        self.mutate()
        self.evaluate(self.children)
        self.select()
        self.print()

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
            for j in range(len(self.children)):
                if self.parents[i].fitness < self.children[j].fitness:
                    self.parents[i] = self.children[j]

    def print(self):
        print(len(self.parents))
        for i in range(len(self.parents)):
            for j in range(len(self.children)):
                print("parent", i, ":", self.parents[i].fitness, "child", j, ":", self.children[j].fitness)
                self.data[i][j] = self.children[j].fitness
            print('\n')


    def show_best(self):
        highest = 0
        highID = c.numberOfGenerations+1
        for i in range(len(self.parents)):
            if self.parents[i].fitness > highest:
                highest = self.parents[i].fitness
                highID = i
        self.parents[highID].start_Simulation("GUI")


    def evaluate(self, solutions):
        for i in range(len(solutions)):
            solutions[i].start_Simulation("DIRECT")
        for i in range(len(solutions)):
            solutions[i].wait_For_Simulation_To_End()