def getMinFlow(mat, tmpPath):
	return min([mat[tmpPath[i]][tmpPath[i+1]] for i in range(len(tmpPath)-1)])


def updateMat(mat, tmpPath, tmpFlow):
	for i in range(len(tmpPath)-1):
		mat[tmpPath[i]][tmpPath[i+1]] -= tmpFlow
		mat[tmpPath[i+1]][tmpPath[i]] += tmpFlow


def getOnePath(mat):
	visited = [False for i in range(len(mat))]
	visited[0] = True
	tmpPath = [0]
	while tmpPath:
		tmp = tmpPath[-1]
		if tmp == len(mat)-1:
			return tmpPath
		for i in range(len(mat)):
			if mat[tmp][i] > 0 and not visited[i]:
				tmpPath.append(i)
				visited[i] = True
				break
		else:
			tmpPath.pop()
	return None


def getFlow(mat):
	maxFlow = 0
	tmpPath = getOnePath(mat)
	while tmpPath is not None:
		print([chr(ord('A') + v) for v in tmpPath])
		tmpFlow = getMinFlow(mat, tmpPath)
		print(tmpFlow)
		maxFlow += tmpFlow
		print(maxFlow)
		updateMat(mat, tmpPath, tmpFlow)
		tmpPath = getOnePath(mat)
	return maxFlow, mat


if __name__ == "__main__":
	mat = [[0, 6, 8, 0, 0, 0], [0, 0, 0, 6, 3, 0], [0, 0, 0, 3, 3, 0], [0, 0, 0, 0, 0, 8], [0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 0]]
	flow, mat = getFlow(mat)
	print(flow)
	# Use networkx to draw the graph
	import networkx as nx
	import matplotlib.pyplot as plt
	G = nx.DiGraph()
	for i in range(len(mat)):
		G.add_node(i, label=chr(ord('A') + i))
	for i in range(len(mat)):
		for j in range(len(mat)):
			if mat[i][j] > 0:
				G.add_edge(i, j, capacity=mat[i][j])
	pos = nx.spring_layout(G)
	nx.draw_networkx_nodes(G, pos)
	nx.draw_networkx_edges(G, pos)
	nx.draw_networkx_labels(G, pos, nx.get_node_attributes(G, 'label'))
	nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, 'capacity'))
	plt.show()

