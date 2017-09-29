import random
import math

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
# Note: If all nodes already covered during the loop, selected_nodes will include (-1)
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

	# Get (node_num, degree) tuples for all nodes
	node_degrees = [(n, degree(n, graph)) for n in graph.keys()]

	# Sort tuples by degree (2nd element in tuple)
	node_degrees.sort(key=lambda pair: pair[1], reverse=True)

	# Keep only the node numbers
	sorted_node_nums = [n for (n, degree) in node_degrees]

	# Get the top k node numbers
	selected_nodes = sorted_node_nums[0:k]

	# Calculate and return coverage based on those last nodes
	return coverage(selected_nodes, graph), selected_nodes



# First, sort selected_nodes by descending order of degree
# Then, select last K*alpha nodes and return those
# Use example: not all the selected people show up to the intervention training
def final_nodes(selected_nodes, graph, alpha):
	K = len(selected_nodes)
	nodes_to_select = math.floor(alpha*K)

	# Get (node_num, degree) tuples for all selected nodes
	selected_node_degrees = [(n, degree(n, graph)) for n in selected_nodes]
	# print(selected_node_degrees)

	# Sort tuples list based on degree (2nd element in pair)
	selected_node_degrees.sort(key=lambda pair: pair[1], reverse=True)
	# print(selected_node_degrees)

	# Keep only the node numbers
	sorted_node_nums = [n for (n, degree) in selected_node_degrees]
	# print(sorted_node_nums)

	# Get last alpha*K nodes
	return sorted_node_nums[-nodes_to_select:]


# Return final coverage given list of initially selected nodes, graph, and alpha
# Alpha controls what fraction of people will show up to the intervention training
def final_coverage(initially_selected_nodes, graph, alpha):
	final_selected_nodes = final_nodes(initially_selected_nodes, graph, alpha)
	return coverage(final_selected_nodes, graph)



# Return average number of neighbors each node in a given graph has
def average_neighbors(graph):
	num_neighbors = [len(graph[n]) for n in graph.keys()]
	avg_neighbors = sum(num_neighbors)/float(len(num_neighbors))
	return avg_neighbors


# random.seed(0)


# x = create_graph(NUM_NODES, 'medium')
# selected_nodes=[5, 100, 40, 60, 70, 31]

# print(coverage(selected_nodes, x))
# print(greedy_coverage(6, x))
# print(degree_coverage(6, x))
# print(random_coverage(6, x))