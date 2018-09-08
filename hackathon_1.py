"Niklaus and Deron parcell"

"Personalized algorithm for cancer therapy with better financial strategy"

import numpy as np 
import random


class energy_usage():

	def __init__(self):
		self.size = 0
		self.how_much = []
		self.spending = 0
		self.money_down = 0

def setup_houses(N):
	# N = number of houses
	neighborhood = []
	for j in range(N):
		rand_num = random.randint(1, 7)  # how many people in the house, this determines energy usage (most-likely)
		neighborhood.append(rand_num)

	return neighborhood


# On average, I found that a house uses probably around 30kwh power a day. Maybe create a range based on how large the household is, and then estimate how much energy they are using
def use_energy(n):
	# n = how many people are in the house
	u = 30  # kwh  (power consumed for 4 people in one day)
	fit = ((n+1)/n)**-1
	usage = u*fit
	return usage 

def money_to_energy():
	
	return 

def pull_energy():
	return

def give_energy():
	return 

def cost():
	return 

###############################################################

e = energy_usage()
e.size = setup_houses(10)
# print(use_energy(e.size[0]))

for j in range(len(e.size)):
	e.how_much.append(use_energy(e.size[j]))


print(e.size)
print(e.how_much)

