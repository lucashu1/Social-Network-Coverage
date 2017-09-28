from networkx import *
import matplotlib.pyplot as plt

# Function 1: convert networkx graph to dictionary representation
def get_neighbors_dict(graph):

	neighbors_dict = {}

	graph = graph.to_directed() # convert to directed in case it's not already

	# get predecessors of each node --> store as neighbors
	for node in graph.nodes():
		neighbors = graph.predecessors(node)
		neighbors_dict[node] = neighbors

	return neighbors_dict

# Function 2: Save a 3 line-plot image for given (graph, k, file_name)
def save_plot(graph, k, file_name):
	# do stuff
	return 0