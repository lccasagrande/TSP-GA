import matplotlib.pyplot as plt
import tsp_ga as ga
import pandas as pd
from random import sample
from mpl_toolkits.basemap import Basemap
import random
import geopandas
import sklearn
from sklearn.cluster import KMeans


def get_genes_from(sample_n=0):
    df = data = pd.read_excel(r'friday_xy_1.xlsx')
    random.seed(1)
    df = df.sample(100).reset_index()

    df = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.x, df.y))



    K_clusters = range(1,10)
    kmeans = [KMeans(n_clusters=i) for i in K_clusters]
    Y_axis = df[['y']]
    X_axis = df[['x']]
    score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]
    # Visualize
    # plt.plot(K_clusters, score)
    # plt.xlabel('Number of Clusters')
    # plt.ylabel('Score')
    # plt.title('Elbow Curve')
    # plt.savefig('kmean')


    kmeans = KMeans(n_clusters = 6, init ='k-means++')
    kmeans.fit(df[df.columns[2:4]]) # Compute k-means clustering.
    df['cluster_label'] = kmeans.fit_predict(df[df.columns[2:4]])
    centers = kmeans.cluster_centers_ # Coordinates of cluster centers.
    labels = kmeans.predict(df[df.columns[2:4]]) # Labels of each point
    df.head(10)

    df.plot.scatter(x = 'x', y = 'y', c=labels, s=50, cmap='viridis')
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.savefig('clusters.png')
    global df
    genes = [ga.Gene(row['USER_Akt_1'], row['y'], row['x'])
             for _, row in df.iterrows()]

    print(genes)

    return genes if sample_n <= 0 else sample(genes, sample_n)

get_genes_from()





def plot(costs, individual, save_to=None):
    plt.figure(1)
    plt.subplot(121)
    plot_ga_convergence(costs)

    plt.subplot(122)
    plot_route(individual)

    if save_to is not None:
        plt.savefig(save_to)
        plt.close()
    else:
        plt.show()

def plot_ga_convergence(costs):
    x = range(len(costs))
    plt.title("GA Convergence")
    plt.xlabel('generation')
    plt.ylabel('cost (KM)')
    plt.text(x[len(x) // 2], costs[0], 'min cost: {} KM'.format(costs[-1]), ha='center', va='center')
    plt.plot(x, costs, '-')


def plot_route(individual):
    m = Basemap(projection='lcc', resolution=None,
                width=5E6, height=5E6,
                lat_0=-15, lon_0=-56)

    plt.axis('off')
    plt.title("Shortest Route")

    for i in range(0, len(individual.genes)):
        x, y = m(individual.genes[i].lng, individual.genes[i].lat)

        plt.plot(x, y, 'ok', c='r', markersize=5)
        if i == len(individual.genes) - 1:
            x2, y2 = m(individual.genes[0].lng, individual.genes[0].lat)
        else:
            x2, y2 = m(individual.genes[i+1].lng, individual.genes[i+1].lat)

        plt.plot([x, x2], [y, y2], 'k-', c='r')
        plt.savefig('plot_route.png')
