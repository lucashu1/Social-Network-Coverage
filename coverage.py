import random

NUM_NODES = 200


# Return a (directed) social network graph of given density
# Graph reprersentation: map from node number to list of neighbors
	# (Directed: Neighbors of node n point to node n)
def create_graph(num_nodes, density='medium'):

	neighbors_list = {} # initialize as empty

	# Sparse: 1-3 neighbors per node
	if density == 'sparse':
		for i in range(num_nodes):
			num_neighbors = random.choice([1, 2, 3])
			neighbors = random.sample(range(num_nodes), num_neighbors)
			neighbors_list[i] = neighbors

	# Medim: 4-7 neighbors per ndoe
	elif density == 'medium':
		for i in range(num_nodes):
			num_neighbors = random.choice([4, 5, 6, 7])
			neighbors = random.sample(range(num_nodes), num_neighbors)
			neighbors_list[i] = neighbors

	# Medim: 8-10 neighbors per ndoe
	elif density == 'dense':
		for i in range(num_nodes):
			num_neighbors = random.choice([8, 9, 10])
			neighbors = random.sample(range(num_nodes), num_neighbors)
			neighbors_list[i] = neighbors

	return neighbors_list


# Return list of neighbors of a node
def neighbors(node, graph):
	return graph[node]


# Takes in a list of selected nodes, and graph representation
# Returns: how many nodes in the given network are covered by the selected nodes
def coverage(selected_nodes, graph):
	covered = set()

	for node in graph.keys():
		for selected_node in selected_nodes:
			if selected_node in neighbors(node, graph) and node not in covered:
				covered.add(node)

	return len(covered)


# Return marginal coverage of selecting one more node
def marginal_coverage(node, selected_nodes, graph):
	current_coverage = coverage(selected_nodes, graph)
	new_coverage = coverage(selected_nodes + [node], graph)
	return new_coverage - current_coverage


# Greedily selects k nodes from network to maximize coverage
# Returns tuple: (final coverage, selected nodes)
def greedy_coverage(k, graph):
	selected_nodes = []

	# Repeat k times:
	while len(selected_nodes) < k:
		current_coverage = coverage(selected_nodes, graph)

		unselected_nodes = set(graph.keys()) - set(selected_nodes)
		curr_best_marg_coverage = 0
		curr_best_node = -1

		# Test each remaining node
		for node in unselected_nodes:
			marg_coverage = marginal_coverage(node, selected_nodes, graph)

			if marg_coverage > curr_best_marg_coverage:
				curr_best_marg_coverage = marg_coverage
				curr_best_node = node

		selected_nodes.append(curr_best_node)

	return coverage(selected_nodes, graph), selected_nodes


# Randomly select k nodes from the graph, find coverage
# Returns tuple: (final coverage, selected nodes)
def random_coverage(k, graph):
	selected_nodes = random.sample(graph.keys(), k)
	return coverage(selected_nodes, graph), selected_nodes


# Find the degree of a given node in a graph
# I.e. How many times this node shows up in other nodes' neighbors lists
def degree(node, graph):
	degree = 0

	for n in graph.keys():
		if node in neighbors(n, graph):
			degree += 1

	return degree


# Return an ascending argsorted list
def argsort(seq):
	return [i for (v, i) in sorted((v, i) for (i, v) in enumerate(seq))]


# Greedily select k nodes with highest degrees, find coverage
# Returns tuple: (final coverage, selected nodes)
def degree_coverage(k, graph):

	# List of degree values for each node
	all_degrees = [degree(n, graph) for n in graph.keys()]

	# Argsort based on degrees, then reverse the list (descending order)
	sorted_nodes = argsort(all_degrees)[::-1]

	# Get k nodes with highest degrees
	selected_nodes = sorted_nodes[0:k]

	return coverage(selected_nodes, graph), selected_nodes


# random.seed(0)


# x = create_graph(NUM_NODES, 'medium')
# selected_nodes=[5, 100, 40, 60, 70, 31]

# print(coverage(selected_nodes, x))
# print(greedy_coverage(6, x))
# print(degree_coverage(6, x))
# print(random_coverage(6, x))