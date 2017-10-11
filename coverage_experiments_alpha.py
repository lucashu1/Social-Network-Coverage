import coverage
import experiment_helpers
import random
from networkx import *
import matplotlib.pyplot as plt

random.seed(0)

MAX_K = 50 # how many people will be selected for the intervention training
ALPHA = 0.3 # controls what proportion of selected people attend the intervention trianing
FINAL_NODES_RAND = True # whether to select final alpha*K nodes randomly
RAND_ITER = 25 # how many times to randomly sample final_nodes, then average final_coverages

X_TICK_FREQ = 5

# ----------------- MEDIUM GRAPHS --------------------

# Generate networkx graphs
erdos_graph_medium = erdos_renyi_graph(200, 0.027, directed=True)
barabasi_graph_medium = barabasi_albert_graph(200,3)
cluster_graph_medium = powerlaw_cluster_graph(200,3, 0.01)

# Convert to neighbor-dictionary representations
erdos_medium = experiment_helpers.get_neighbors_dict(erdos_graph_medium)
barabasi_medium = experiment_helpers.get_neighbors_dict(barabasi_graph_medium)
cluster_medium = experiment_helpers.get_neighbors_dict(cluster_graph_medium)

# # Make sure graphs have medium density
# print("Erdos (Medium) Neighbors: ", coverage.average_neighbors(erdos_medium))
# print("Barabasi (Medium) Neighbors: ", coverage.average_neighbors(barabasi_medium))
# print("Cluster (Medium) Neighbors: ", coverage.average_neighbors(cluster_medium))

# Generate plots
experiment_helpers.make_plot(erdos_medium, K=MAX_K, \
	plot_title="Erdos-Renyi (Medium) Graph Coverage\nn = 200, p = 0.027, alpha = 0.3, samples = 25", \
	file_name='erdos_medium_alpha03.png', alpha=ALPHA, x_tick_freq=X_TICK_FREQ, \
	rand=FINAL_NODES_RAND, rand_iter=RAND_ITER)

experiment_helpers.make_plot(barabasi_medium, K=MAX_K, \
	plot_title="Barabasi-Albert (Medium) Graph Coverage\nn = 200, m = 3, alpha = 0.3, samples = 25", \
	file_name='barabasi_medium_alpha03.png', alpha=ALPHA, x_tick_freq=X_TICK_FREQ, \
	rand=FINAL_NODES_RAND, rand_iter=RAND_ITER)

experiment_helpers.make_plot(cluster_medium, K=MAX_K, \
	plot_title="Powerlaw Cluster (Medium) Graph Coverage\nn = 200, m = 3, p = 0.01, alpha = 0.3, samples = 25", \
	file_name='cluster_medium_alpha03.png', alpha=ALPHA, x_tick_freq=X_TICK_FREQ, \
	rand=FINAL_NODES_RAND, rand_iter=RAND_ITER)




# ----------------- SPARSE GRAPHS --------------------

# Generate networkx graphs
erdos_graph_sparse = erdos_renyi_graph(200, 0.01, directed=True)
barabasi_graph_sparse = barabasi_albert_graph(200,1)
cluster_graph_sparse = powerlaw_cluster_graph(200,1, 0.01)

# Convert to neighbor-dictionary representations
erdos_sparse = experiment_helpers.get_neighbors_dict(erdos_graph_sparse)
barabasi_sparse = experiment_helpers.get_neighbors_dict(barabasi_graph_sparse)
cluster_sparse = experiment_helpers.get_neighbors_dict(cluster_graph_sparse)

# # Make sure graphs have low density
# print("Erdos (Sparse) Neighbors: ", coverage.average_neighbors(erdos_sparse))
# print("Barabasi (Sparse) Neighbors: ", coverage.average_neighbors(barabasi_sparse))
# print("Cluster (Sparse) Neighbors: ", coverage.average_neighbors(cluster_sparse))

# Generate plots
experiment_helpers.make_plot(erdos_sparse, K=MAX_K, \
	plot_title="Erdos-Renyi (Sparse) Graph Coverage\nn = 200, p = 0.01, alpha = 0.3, samples = 25", \
	file_name='erdos_sparse_alpha03.png', alpha=ALPHA, x_tick_freq=X_TICK_FREQ, \
	rand=FINAL_NODES_RAND, rand_iter=RAND_ITER)

experiment_helpers.make_plot(barabasi_sparse, K=MAX_K, \
	plot_title="Barabasi-Albert (Sparse) Graph Coverage\nn = 200, m = 1, alpha = 0.3, samples = 25", \
	file_name='barabasi_sparse_alpha03.png', alpha=ALPHA, x_tick_freq=X_TICK_FREQ, \
	rand=FINAL_NODES_RAND, rand_iter=RAND_ITER)

experiment_helpers.make_plot(cluster_sparse, K=MAX_K, \
	plot_title="Powerlaw Cluster (Sparse) Graph Coverage\nn = 200, m = 1, p = 0.01, alpha = 0.3, samples = 25", \
	file_name='cluster_sparse_alpha03.png', alpha=ALPHA, x_tick_freq=X_TICK_FREQ, \
	rand=FINAL_NODES_RAND, rand_iter=RAND_ITER)




# ----------------- DENSE GRAPHS --------------------

# Generate networkx graphs
erdos_graph_dense = erdos_renyi_graph(200, 0.05, directed=True)
barabasi_graph_dense = barabasi_albert_graph(200,5)
cluster_graph_dense = powerlaw_cluster_graph(200,5, 0.01)

# Convert to neighbor-dictionary representations
erdos_dense = experiment_helpers.get_neighbors_dict(erdos_graph_dense)
barabasi_dense = experiment_helpers.get_neighbors_dict(barabasi_graph_dense)
cluster_dense = experiment_helpers.get_neighbors_dict(cluster_graph_dense)

# # Make sure graphs have high density
# print("Erdos (Dense) Neighbors: ", coverage.average_neighbors(erdos_dense))
# print("Barabasi (Dense) Neighbors: ", coverage.average_neighbors(barabasi_dense))
# print("Cluster (Dense) Neighbors: ", coverage.average_neighbors(cluster_dense))

# Generate plots
experiment_helpers.make_plot(erdos_dense, K=MAX_K, \
	plot_title="Erdos-Renyi (Dense) Graph Coverage\nn = 200, p = 0.05, alpha = 0.3, samples = 25", \
	file_name='erdos_dense_alpha03.png', alpha=ALPHA, x_tick_freq=X_TICK_FREQ, \
	rand=FINAL_NODES_RAND, rand_iter=RAND_ITER)

experiment_helpers.make_plot(barabasi_dense, K=MAX_K, \
	plot_title="Barabasi-Albert (Dense) Graph Coverage\nn = 200, m = 5, alpha = 0.3, samples = 25", \
	file_name='barabasi_dense_alpha03.png', alpha=ALPHA, x_tick_freq=X_TICK_FREQ, \
	rand=FINAL_NODES_RAND, rand_iter=RAND_ITER)

experiment_helpers.make_plot(cluster_medium, K=MAX_K, \
	plot_title="Powerlaw Cluster (Dense) Graph Coverage\nn = 200, m = 5, p = 0.01, alpha = 0.3, samples = 25", \
	file_name='cluster_dense_alpha03.png', alpha=ALPHA, x_tick_freq=X_TICK_FREQ, \
	rand=FINAL_NODES_RAND, rand_iter=RAND_ITER)


