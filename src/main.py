import utils
import random
import argparse
import tsp_ga as ga
from datetime import datetime
from data import Gene
from pool import Population
import pool as pl
from random import sample
import numpy as np
def run(args):

    # n_clusters = args.nvehicles 
    df = utils.get_genes_from(args.cities_fn, args.nvehicles)
    


    for i in range(args.nvehicles):
        clus = df.loc[df['cluster_label'] == i]
        clus
        clus.loc[len(clus.index)] = [0,'Depot', 69.71059355829574, 19.01346092171551, None, i]
        print(clus)

        genes = [ga.Gene(row['USER_Akt_1'], row['y'], row['x'])
            for _, row in clus.iterrows()]
        # sample_n = random.randint(4,np.round(len(clus))) #Ensuring sample_n changes each time
        sample_n = 0

        if sample_n <= 0:
            genes = genes
        else: 
            genes = sample(genes, sample_n) #



        if args.verbose:
            print("-- Running TSP-GA with {} cities --".format(len(genes)))



        history = pl.run_ga(genes, args.pop_size, args.n_gen,
                            args.tourn_size, args.mut_rate, args.verbose)

        if args.verbose:
            print("-- Drawing Route --")

        utils.plot(history['cost'], history['route'])

        if args.verbose:
            print("-- Done --")



# class Vehicle():
#     def __init__():
#         self.max_speed = 10

#     def rule_1(self, neighbours):
#         for vehicle in neighbours:





if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', type=int, default=1)
    parser.add_argument('--pop_size', type=int, default=500, help='Population size')
    parser.add_argument('--tourn_size', type=int, default=50, help='Tournament size')
    parser.add_argument('--mut_rate', type=float, default=0.02, help='Mutation rate')
    parser.add_argument('--n_gen', type=int, default=20, help='Number of equal generations before stopping')
    parser.add_argument('--cities_fn', type=str, default="data/cities.csv", help='Data containing the geographical coordinates of cities')
    parser.add_argument('--nvehicles', type =int , default = 5, help = 'Number of vehicles available')

    random.seed(datetime.now())
    args = parser.parse_args()

    if args.tourn_size > args.pop_size:
        raise argparse.ArgumentTypeError('Tournament size cannot be bigger than population size.')

    run(args)