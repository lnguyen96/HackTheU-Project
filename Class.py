class house:
	def __init__(self, n, s):
		self.name = n
		self.size = s
		self.usage = (30*self.size)/(self.size+1)

	def add_human(self, n):
		self.size += n
		self.usage = (30*self.size)/(self.size+1)

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

reserve = 0

h1 = house('1', 1)
h2 = house('2', 2)
h3 = house('3', 3)

print(h1.size, h1.usage)
h1.add_human(2)
print(h1.size, h1.usage)

graph = {h1:[h2],
		h2 : [h3]}

print(find_path(graph, h1, h3))