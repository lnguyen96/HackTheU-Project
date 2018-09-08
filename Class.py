class house:
	def __init__(self, n, c):
		self.name = n
		self.cost = c

reserve = 0

h1 = house('1', 1)
h2 = house('2', 2)
h3 = house('3', 3)

graph = {h1:[h2],
		h2 : [h3]}

def find_path(graph, start, end, path=[]):
	path = path + [start.name]
	#print(path)
	if start == end:
		return path
	if start not in graph:
		return None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path)
			if newpath: return newpath
	return None

print(find_path(graph, h1, h3))