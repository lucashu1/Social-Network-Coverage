import coverage
import experiment_helpers
import random
from networkx import *
import matplotlib.pyplot as plt

random.seed(0)

MAX_K = 20

erdos_graph = erdos_renyi_graph(100, 0.05, directed=True)
barabasi_graph = barabasi_albert_graph(100,2)

# convert to dictionary representation
erdos = experiment_helpers.get_neighbors_dict(erdos_graph)
barabasi = experiment_helpers.get_neighbors_dict(barabasi_graph)


# Get coverages on erdos graph for k: 1-20
erdos_degree_coverages = []
erdos_greedy_coverages = []
erdos_random_coverages = []

for i in range(1, MAX_K+1):
	greedy_coverage = coverage.greedy_coverage(i, erdos)[0]
	degree_coverage = coverage.degree_coverage(i, erdos)[0]
	random_coverage = coverage.random_coverage(i, erdos)[0]

	erdos_greedy_coverages.append(greedy_coverage)
	erdos_degree_coverages.append(degree_coverage)
	erdos_random_coverages.append(random_coverage)



# Get coverages on barabasi graph for k: 1-20
barabasi_greedy_coverages = []
barabasi_degree_coverages = []
barabasi_random_coverages = []

for i in range(1, MAX_K+1):
	greedy_coverage = coverage.greedy_coverage(i, barabasi)[0]
	degree_coverage = coverage.degree_coverage(i, barabasi)[0]
	random_coverage = coverage.random_coverage(i, barabasi)[0]
	
	barabasi_greedy_coverages.append(greedy_coverage)
	barabasi_degree_coverages.append(degree_coverage)
	barabasi_random_coverages.append(random_coverage)
	

# Generate Erdos-Renyi plot
plt.plot(range(1, MAX_K+1), erdos_greedy_coverages)
plt.plot(range(1, MAX_K+1), erdos_degree_coverages)
plt.plot(range(1, MAX_K+1), erdos_random_coverages)
plt.title("Erdos-Renyi Graph Coverage\nn = 100, p = 0.05")
plt.xticks(range(0, 21, 2))
plt.xlabel("K (number of nodes selected)")
plt.ylabel("Nodes covered")
plt.legend(['Greedy', 'High-Degree', 'Random'], loc='upper left')
plt.savefig('erdos.png')

plt.clf()

# Generate Barabasi-Albert plot
plt.plot(range(1, MAX_K+1), barabasi_greedy_coverages)
plt.plot(range(1, MAX_K+1), barabasi_degree_coverages)
plt.plot(range(1, MAX_K+1), barabasi_random_coverages)
plt.title("Barabasi-Albert Graph Coverage\nn=100 m = 2")
plt.xticks(range(0, 21, 2))
plt.xlabel("K (number of nodes selected)")
plt.ylabel("Nodes covered")
plt.legend(['Greedy', 'High-Degree', 'Random'], loc='upper left')
plt.savefig('barabasi.png')

