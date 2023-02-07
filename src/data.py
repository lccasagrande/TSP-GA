from sys import maxsize
from time import time
from random import random, randint, sample
from haversine import haversine

class Gene:  # City
    # keep distances from cities saved in a table to improve execution time.
    __distances_table = {}

    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng

    def get_distance_to(self, dest):
        origin = (self.lat, self.lng)
        dest = (dest.lat, dest.lng)

        forward_key = origin + dest
        backward_key = dest + origin

        if forward_key in Gene.__distances_table:
            return Gene.__distances_table[forward_key]

        if backward_key in Gene.__distances_table:
            return Gene.__distances_table[backward_key]

        dist = int(haversine(origin, dest))
        Gene.__distances_table[forward_key] = dist

        return dist