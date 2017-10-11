# exact baseline
import gurobipy as gp

#adj = neighbour_dict
def create_invitees_list(possible_adj):

	# print(possible_adj[2])

	invitees = []
	for e in possible_adj.keys():
		ngh = possible_adj[e]
		for n in ngh: 
			if n not in invitees: # if it has already not been added
				invitees.append(n)


	# print(invitees)
	
		
	return invitees
	
# cur_invitees = create_invitees_list(cur_adj)
 

#budget = k
#cur_key_list = adj.keys()
#cur_adj = adj
#cur_invites = create_invitees_list(cur_adj)

'''
	Below is the exact solution to the coverage problem, no approximations
	Greedy was an approximation technique.
	This function returns 3 quantities
	(1) monitors : selected_nodes
	(2) those covered
	(3) total count of how many covered
	* We are only interested in (1) from this output.
'''
def coverage_optimize(budget,key_list,adj,cur_invitees):
	m = gp.Model('Moniter selection no time dependency')
	
	# #binary variable for each of the nodes in the network
	# #x_i = {1 , if i is a monitor otherwise 0}
	
	x = []
	for i in range(0, len(cur_invitees)):
		x.append(m.addVar(vtype = gp.GRB.BINARY, name = 'x_' + str(i)))
		
	#coverage
	y = []
	for i in range(0,len(key_list)):
		y.append(m.addVar(vtype = gp.GRB.BINARY, name = 'y_' + str(i)))
		
		
	m.update()

	
	#add budget constraint - total no. of monitors <= alphaK #alpha participation rate
	
	m.addConstr(gp.quicksum(x)<=budget)

	#coverage constraint
	for i in range(0,len(key_list)):
		n = adj[key_list[i]]
		x_list = []
		#visited = 0
		for j in n:
			x_list.append(x[cur_invitees.index(j)])
		m.addConstr(y[i] <= gp.quicksum(x_list))
				
	m.setObjective(gp.quicksum(y), gp.GRB.MAXIMIZE)
	
	m.optimize()
	
	monitors = []
	covered_nodes = []
	sum_covered = 0
	for v in m.getVars():
		if v.varName[0] == 'x':
			if v.x == 1:
				v_data = v.varName.split("_")
				monitor_index = int(v_data[1])
				monitors.append(cur_invitees[monitor_index])
		if v.varName[0] == 'y':
			if v.x == 1:
				sum_covered +=1
				v_data = v.varName.split("_")
				covered_index = int(v_data[1])
				covered_nodes.append(key_list[covered_index])
				
				
	return [monitors,sum_covered,covered_nodes]
