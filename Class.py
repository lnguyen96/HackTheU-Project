class house:
	def __init__(self, n, s): #name of house, how many people in the house
		self.name = n
		self.size = s
		#initial usage
		self.usage_i = (60*self.size)/(self.size+1)
		#initialize usage
		self.usage = self.usage_i

	def add_energy(self, e): #adds energy into the house
		self.usage += e

	def sub_energy(self, e): #takes energy away from the house if it can, else explain why it can't
		if(self.usage == 0): #no energy to give 
			print("No energy to give")
			return False
		elif(self.usage - e < 0): #not enough energy to give 
			print("Not enough energy to give, remaining " + str(self.usage))
			return False
		else:
			print("Gave reserve " + str(e) + " kWh") #no problem
			self.usage -= e
			return True

	def net_change(self): #calculate net change for end of month cost
		print("Net change of " + str(self.usage - self.usage_i) + " kWh")

class reserve:
	def __init__(self, n, e): #name of reserve, how much energy it has
		self.name = n
		self.energy = e

	def add_energy(self, e): #add energy to the reserve
		self.energy += e

	def sub_energy(self, e): #takes away energy from reserve if it can, else explain why it can't
		if(self.energy == 0): #no energy to give 
			print("No energy to give")
			return False
		elif(self.energy - e < 0): #not enough energy to give 
			print("Not enough energy to give, remaining " + str(self.energy))
			return False
		else:
			print("Gave house " + str(e) + " kWh") #no problem
			self.energy -= e
			return True

def add(graph, house, reserve, energy): #adds the energy to the house 
	if(reserve.sub_energy(energy)): #checks if you can take energy from reserve 
		house.add_energy(energy) #performs the transfer

def sub(graph, house, reserve, energy): #adds the energy to the house
	if(house.sub_energy(energy)): #checks if you can take energy from house
		reserve.add_energy(energy) #performs the transfer

def find_path(graph, start, end, path=[]): #path checker
	path = path + [start.name]
	if start == end:
		return path
	if start not in graph:
		return None
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph, node, end, path)
			if newpath: return newpath
	return None
	
'''
#####################################################
#                   Test Cases                      #
#####################################################
'''
h1 = house('1', 1) 
h2 = house('2', 2)
h3 = house('3', 3)

r1 = reserve('1r', 300)

graph = {r1: [h1, h2, h3]}

print(find_path(graph, r1, h3))

add(graph, h1, r1, 30)

print(h1.usage)

h1.net_change()