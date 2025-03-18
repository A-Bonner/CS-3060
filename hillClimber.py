from solution import SOLUTION
import constants as c
import copy as copy

class HILLCLIMBER:
    def __init__(self):
        self.parent = SOLUTION()

    def evolve(self):
        self.parent.evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.evolve_For_One_Generation()

    def evolve_For_One_Generation(self):
        self.spawn()
        self.mutate()
        self.child.evaluate("DIRECT")
        self.print()
        self.select()

    def spawn(self):
        self.child = copy.deepcopy(self.parent)

    def mutate(self):
        self.child.mutate()

    def select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def print(self):
        print(self.parent.fitness, self.child.fitness)

    def show_best(self):
        self.parent.evaluate("GUI")