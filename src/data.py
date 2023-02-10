from sys import maxsize
from time import time
from random import random, randint, sample
from haversine import haversine
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class Gene:  # City
    # keep distances from cities saved in a table to improve execution time.
    __distances_table = {}

    def __init__(self, name, lat, lng, cluster):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.cluster = cluster

        
    def get_distance_to(self, dest):
        origin = (self.lat, self.lng)
        dest = (dest.lat, dest.lng)

        forward_key = origin + dest
        backward_key = dest + origin
        # print(forward_key)
        # print(backward_key)

        if forward_key in Gene.__distances_table:
            return Gene.__distances_table[forward_key]

        if backward_key in Gene.__distances_table:
            return Gene.__distances_table[backward_key]

        dist = int(haversine(origin, dest, unit = 'm'))
        Gene.__distances_table[forward_key] = dist

        return dist




        



