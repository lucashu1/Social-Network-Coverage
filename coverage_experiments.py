import coverage
import experiment_helpers
import random
from networkx import *
import matplotlib.pyplot as plt

random.seed(0)

MAX_K = 20

# Generate networkx graphs
erdos_graph = erdos_renyi_graph(100, 0.05, directed=True)
barabasi_graph = barabasi_albert_graph(100,2)
cluster_graph = powerlaw_cluster_graph(100,2, 0.01)

# Convert to neighbor-dictionary representations
erdos = experiment_helpers.get_neighbors_dict(erdos_graph)
barabasi = experiment_helpers.get_neighbors_dict(barabasi_graph)
cluster = experiment_helpers.get_neighbors_dict(cluster_graph)


# Make them plots!
experiment_helpers.make_plot(erdos, K=MAX_K, \
	plot_title="Erdos-Renyi Graph Coverage\nn = 100, p = 0.05", \
	file_name='erdos.png', x_tick_freq=2)

experiment_helpers.make_plot(barabasi, K=MAX_K, \
	plot_title="Barabasi-Albert Graph Coverage\nn=100 m = 2", \
	file_name='barabasi.png', x_tick_freq=2)

experiment_helpers.make_plot(cluster, K=MAX_K, \
	plot_title="Powerlaw Cluster Graph Coverage\nn=100 m = 2 p = 0.01", \
	file_name='cluster.png', x_tick_freq=2)

