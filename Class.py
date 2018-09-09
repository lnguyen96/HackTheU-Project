import pandas as pd
import csv
import math
import numpy as np 
import random
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 

class house:
	def __init__(self, n, s): #name of house, how many people in the house
		self.name = n
		self.size = s
		#initial usage
		self.usage_i = (60*self.size)/(self.size+1)
		#initialize usage
		self.usage = self.usage_i

	def add_energyh(self, e): #adds energy into the house
		print("Gave house " + str(e) + " kWh") #energy added to reserve
		self.usage += e

	def sub_energyh(self, e): #takes energy away from the house if it can, else explain why it can't
		if(self.usage == 0): #no energy to give 
			print("No energy to give")
			return False
		elif(self.usage - e < 0): #not enough energy to give 
			print("Not enough energy to give, remaining " + str(self.usage))
			return False
		else:
			self.usage -= e
			return True

	def net_change(self): #calculate net change for end of month cost
		print("Net change of " + str(self.usage - self.usage_i) + " kWh")

class reserve:
	def __init__(self, n, e): #name of reserve, how much energy it has
		self.name = n
		self.energy = e

	def add_energyr(self, e): #add energy to the reserve
		print("Gave reserve " + str(e) + " kWh") #energy is added
		self.energy += e

	def sub_energyr(self, e): #takes away energy from reserve if it can, else explain why it can't
		if(self.energy == 0): #no energy to give 
			print("No energy to give")
			return False
		elif(self.energy - e < 0): #not enough energy to give 
			print("Not enough energy to give, remaining " + str(self.energy))
			return False
		else:
			self.energy -= e
			return True

def add(graph, house, reserve, energy): #adds the energy to the house 
	if(reserve.sub_energyr(energy) and check_connect(graph, house, reserve)): #checks if you can take energy from reserve 
		house.add_energyh(energy) #performs the transfer

def sub(graph, house, reserve, energy): #adds the energy to the house
	if(house.sub_energyh(energy) and check_connect(graph, house, reserve)): #checks if you can take energy from house
		reserve.add_energyr(energy) #performs the transfer

def check_connect(graph, house, reserve): #checks if house is connected to reserve
	if(house.name in graph[reserve.name]):
		return True
	else:
		return False


######################################################################################################################################
def money_to_energy():
	S_upper = 80
	S_lower = 50
	num = random.randint(S_lower, S_upper)
	return num

def pull_energy(N):  # N is the money put in per month
	# amount to pull
	am_to_pull = N + random.randint(-10, 10)  # kWh
	return am_to_pull


######################################################################################################################################
#####################################################
#                   Test Cases                      #
#####################################################

h = []
r = []
graph = {}
kWh = 1.26

with open('hhSizeAndName.csv') as data:
	csvReader = csv.reader(data)
	next(data)
	for row in csvReader:
		h.append(house(row[1],int(row[0])))

numReserve = math.ceil(len(h)/10)
for i in range(0, numReserve):
	r.append(reserve("r"+str(i), money_to_energy()))

for i in range(0,numReserve):
	for j in range(0,10):
		try:
			if(r[i].name not in graph):
				graph[r[i].name] = [h[j+(i*10)].name]
			else:
				graph[r[i].name].append(h[j+(i*10)].name)
		except:
			pass

for i in range(0,len(h)):
	h[i].usage += pull_energy(kWh*h[i].usage_i)

for i in range(0, numReserve):
	for j in range(0,numReserve):
		if(r[j].name not in graph[r[i].name] and r[j].name != r[i].name):
					graph[r[i].name].append(r[j].name)

#print(graph[r[1].name])
print(graph)


print(h[5].usage)
print(r[0].energy)
add(graph, h[0], r[0], 30)
sub(graph, h[0], r[0], 30)