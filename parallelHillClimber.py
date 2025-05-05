from solution import SOLUTION
import constants as c
import copy as copy
import os as os
import numpy as numpy
import time as time

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
            print("Generation", currentGen)
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
            #print("parent", i, ":", self.parents[i].fitness, "child", j, ":", self.children[j].fitness)
            self.data[i][gen] = self.children[i].fitness
            #print('\n')
    """
    def select(self):

        file = open("bestParents.txt", "w")
        best_in_round = 0
        best_key = 0
        best_is_child = True

        for key in self.parents.keys():
            #print("child: ", self.children[key].fitness)
            #print("parent: ", self.parents[key].fitness)
            if(self.children[key].fitness > self.parents[key].fitness):
                self.parents[key] = self.children[key]
               # print("parent: ", self.parents[key].fitness)
            if(self.children[key].fitness > best_in_round):
                best_in_round = self.children[key].fitness
                best_key = key
                best_is_child = True
            if(self.parents[key].fitness > best_in_round):
                best_in_round = self.parents[key].fitness
                best_key = key
                best_is_child = False
        if best_is_child == True:
            file.write(str(self.children[best_key]) +  "," + str(self.children[best_key].fitness) + "\n")
        else:
            file.write(str(self.parents[best_key]) +  "," + str(self.parents[best_key].fitness))
        file.close()
    """

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