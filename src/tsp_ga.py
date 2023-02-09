from sys import maxsize
from time import time
from random import random, randint, sample
from haversine import haversine
from data import Gene




class Individual:  # Route: possible solution to TSP
    def __init__(self, genes):
        assert(len(genes) > 2)
        self.genes = genes
        self.__reset_params()

    def swap(self, gene_1, gene_2):
        self.genes[0]
        a, b = self.genes.index(gene_1), self.genes.index(gene_2)
        self.genes[b], self.genes[a] = self.genes[a], self.genes[b]
        self.__reset_params()

    def add(self, gene):
        self.genes.append(gene)
        self.__reset_params()

    @property
    def fitness(self):
        if self.__fitness == 0:
            self.__fitness = 1 /( self.travel_cost + 10e-9) # Normalize travel cost
            # print(self.travel_cost)
        return self.__fitness

    @property
    def travel_cost(self):  # Get total travelling cost
        if self.__travel_cost == 0:
            for i in range(len(self.genes)):
                origin = self.genes[i]
                if i == len(self.genes) - 1:
                    dest = self.genes[0]
                else:
                    dest = self.genes[i+1]

                self.__travel_cost += origin.get_distance_to(dest)
        # print(self.__travel_cost)

        return self.__travel_cost

    def __reset_params(self):
        self.__travel_cost = 0
        self.__fitness = 0


