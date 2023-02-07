import utils
import random
import argparse
import tsp_ga as ga
from datetime import datetime
from data import Gene
from pool import Population
import pool as pl

def run(args):
    genes = utils.get_genes_from(args.cities_fn)

    if args.verbose:
        print("-- Running TSP-GA with {} cities --".format(len(genes)))

    history = pl.run_ga(genes, args.pop_size, args.n_gen,
                        args.tourn_size, args.mut_rate, args.verbose)

    if args.verbose:
        print("-- Drawing Route --")

    utils.plot(history['cost'], history['route'])

    if args.verbose:
        print("-- Done --")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose', type=int, default=1)
    parser.add_argument('--pop_size', type=int, default=500, help='Population size')
    parser.add_argument('--tourn_size', type=int, default=50, help='Tournament size')
    parser.add_argument('--mut_rate', type=float, default=0.02, help='Mutation rate')
    parser.add_argument('--n_gen', type=int, default=20, help='Number of equal generations before stopping')
    parser.add_argument('--cities_fn', type=str, default="data/cities.csv", help='Data containing the geographical coordinates of cities')

    random.seed(datetime.now())
    args = parser.parse_args()

    if args.tourn_size > args.pop_size:
        raise argparse.ArgumentTypeError('Tournament size cannot be bigger than population size.')

    run(args)