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
# rand: whether or not to sample final_nodes randomly from selected_nodes
# rand_iter: how many times to sample final_nodes (-1 by default --> just sample once)
def make_plot(graph, K, plot_title, file_name, alpha = -1, x_tick_freq=2, rand=False, rand_iter=-1):
	
	# Clear plt just in case
	plt.clf()

	# Get coverages on graph for k: 1-K
	degree_coverages = []
	greedy_coverages = []
	random_coverages = []

	for i in range(1, K+1):

		# If no alpha given: use all selected nodes
		if alpha == -1:
			greedy_coverage = coverage.greedy_coverage(i, graph)[0]
			degree_coverage = coverage.degree_coverage(i, graph)[0]
			random_coverage = coverage.random_coverage(i, graph)[0]

			greedy_coverages.append(greedy_coverage)
			degree_coverages.append(degree_coverage)
			random_coverages.append(random_coverage)

		# If given alpha: assume not everyone attends the training
		else:

			# By default, only randomly sample final_nodes once
			if rand_iter == -1:

				# Get selected_nodes using each method
				greedy_nodes = coverage.greedy_coverage(i, graph)[1]
				degree_nodes = coverage.degree_coverage(i, graph)[1]
				random_nodes = coverage.random_coverage(i, graph)[1]

				# Get final_coverage from selected_nodes
				greedy_coverages.append(coverage.final_coverage(greedy_nodes, graph, alpha, rand))
				degree_coverages.append(coverage.final_coverage(degree_nodes, graph, alpha, rand))
				random_coverages.append(coverage.final_coverage(random_nodes, graph, alpha, rand))

			# If rand_iter specified: randomly sample final_nodes multiple times, 
			# then average over final_coverage values
			else:

				# Get selected_nodes using each method
				greedy_nodes = coverage.greedy_coverage(i, graph)[1]
				degree_nodes = coverage.degree_coverage(i, graph)[1]
				random_nodes = coverage.random_coverage(i, graph)[1]

				greedy_tracker = []
				degree_tracker = []
				random_tracker = []

				# Keep sample final_nodes to get final_coverages
				for i in range(rand_iter):
					greedy_tracker.append(coverage.final_coverage(greedy_nodes, graph, alpha, rand))
					degree_tracker.append(coverage.final_coverage(degree_nodes, graph, alpha, rand))
					random_tracker.append(coverage.final_coverage(random_nodes, graph, alpha, rand))

				# Average over each sampling iteration
				greedy_avg = sum(greedy_tracker)/float(len(greedy_tracker))
				degree_avg = sum(degree_tracker)/float(len(degree_tracker))
				random_avg = sum(random_tracker)/float(len(random_tracker))

				greedy_coverages.append(greedy_avg)
				degree_coverages.append(degree_avg)
				random_coverages.append(random_avg)

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

