from networkx import *
import coverage
import matplotlib.pyplot as plt

# Convert networkx graph to dictionary representation
def get_neighbors_dict(graph):

	neighbors_dict = {}

	graph = graph.to_directed() # convert to directed in case it's not already

	# get predecessors of each node --> store as neighbors
	for node in graph.nodes():
		neighbors = graph.predecessors(node)
		neighbors_dict[node] = neighbors

	return neighbors_dict



# Takes in a graph in neighbor-dict representation
# Save a 3 line-plot image for given (graph, k, file_name)
def make_plot(graph, K, plot_title, file_name, alpha = -1, x_tick_freq=2):
	
	# Clear plt just in case
	plt.clf()

	# Get coverages on graph for k: 1-K
	degree_coverages = []
	greedy_coverages = []
	random_coverages = []

	for i in range(1, K+1):

		# If no alpha given: assume all nodes selected 
		if alpha == -1:
			greedy_coverage = coverage.greedy_coverage(i, graph)[0]
			degree_coverage = coverage.degree_coverage(i, graph)[0]
			random_coverage = coverage.random_coverage(i, graph)[0]

			greedy_coverages.append(greedy_coverage)
			degree_coverages.append(degree_coverage)
			random_coverages.append(random_coverage)

		# If given alpha: assume not everyone attends the training
		else:
			greedy_nodes = coverage.greedy_coverage(i, graph)[1]
			degree_nodes = coverage.degree_coverage(i, graph)[1]
			random_nodes = coverage.random_coverage(i, graph)[1]

			greedy_coverages.append(coverage.final_coverage(greedy_nodes, graph, alpha))
			degree_coverages.append(coverage.final_coverage(degree_nodes, graph, alpha))
			random_coverages.append(coverage.final_coverage(random_nodes, graph, alpha))

	# Create the plot
	plt.plot(range(1, K+1), greedy_coverages)
	plt.plot(range(1, K+1), degree_coverages)
	plt.plot(range(1, K+1), random_coverages)
	plt.title(plot_title)
	plt.xticks(range(0, K+1, x_tick_freq))
	plt.xlabel("K (number of nodes selected)")
	plt.ylabel("Nodes covered")
	plt.legend(['Greedy', 'High-Degree', 'Random'], loc='upper left')
	plt.savefig(file_name)
	plt.clf()

