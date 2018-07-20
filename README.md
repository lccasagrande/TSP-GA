## Overview
This repository contains a generic Python implementation of a Genetic Algorithm to solve the Travelling Salesman Problem (TSP). Geographic coordinates of cities are provided as input to generate a edge-weighted complete graph where the weights are the distance between the cities in kilometers.

## Output Example

![output-ga](https://i.imgur.com/Zkj0z7m.png)

## Requirements
You'll need Python 3.x x64 to be able to run theses projects.

If you do not have Python installed yet, it is recommended that you install the [Anaconda](https://www.anaconda.com/download/) distribution of Python, which has almost all packages required in these project.

You can also install Python 3.x x64 from [here](https://www.python.org/downloads/)

## Instructions
1. Clone the repository and navigate to the downloaded folder.
    ```bash
    git clone https://github.com/lccasagrande/TSP-GA.git
    cd TSP-GA
    ```

2. Install required packages:
	```bash
	pip install -e .
	```
    Or:
	```bash
	pip install -e . --user
	```

3. Navigate to the src folder and execute:
    ```bash
    cd src
    python main.py -v 1 --pop_size 500 --tourn_size 50 --mut_rate 0.02 --n_gen 20 --cities_fn '../data/cities.csv'
    ```

