from solution import SOLUTION
import constants as c
import copy as copy
import os as os
import numpy as numpy

class PARALLELHILLCLIMBER:
    def __init__(self):
        os.system("del brain*.nndf")
        os.system("del fitness*.txt")
        os.system("del sensor*.txt")
        self.nextAvailableID = 0
        self.parents = {}
        self.data = numpy.zeros([c.populationSize, c.numberOfGenerations])
        for i in range(0, c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def evolve(self):
        self.evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.evolve_For_One_Generation()

    def evolve_For_One_Generation(self):
        self.spawn()
        self.mutate()
        self.evaluate(self.children)
        self.print()
        self.select()

    def spawn(self):
        self.children = {}
        for i in self.parents.keys():
            self.children[i] = copy.deepcopy(self.parents[i])
            self.children[i].set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def mutate(self):
        for i in range(0, len(self.children)):
            self.children[i].mutate()

    def select(self):
        for i in range(0, len(self.parents)):
            for j in range(0, len(self.children)):
                if self.parents[i].fitness < self.children[j].fitness:
                    self.parents[i] = self.children[j]

    def print(self):
        for i in range(0, len(self.parents)):
            for j in range(0, len(self.children)):
                print(self.parents[i].fitness, self.children[j].fitness)
                self.data[i][j] = self.children[i].fitness
            print()

    def show_best(self):
        highest = 0
        highID = c.numberOfGenerations+1
        for i in range(0, len(self.parents)):
            if self.parents[i].fitness > highest:
                highest = self.parents[i].fitness
                highID = i
        self.parents[highID].start_Simulation("GUI")


    def evaluate(self, solutions):
        for i in range(0, len(solutions)):
            solutions[i].start_Simulation("DIRECT")
        for i in range(0, len(solutions)):
            solutions[i].wait_For_Simulation_To_End()
