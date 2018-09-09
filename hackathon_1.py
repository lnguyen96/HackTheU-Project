"Niklaus Parcell, Deron parcell, Long Nguyen, Edwin Chiang"

"Personalized algorithm for cancer therapy with better financial strategy"

import numpy as np 
import random
import matplotlib.pyplot as plt 


class energy_usage():
	def __init__(self):
		self.size = 0
		self.how_much = []  # how much energy at a house
		self.spending = []
		self.money_down = 0

class energy_reserve():
	def __init__(self):
		self.stored_energy = []

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
	u = 60  # kwh  (power consumed for 4 people in one day)
	fit = ((n+1)/n)**-1
	usage = u*fit
	return usage 

def money_to_energy():
	S_upper = 80
	S_lower = 50
	num = random.randint(S_lower, S_upper)
	return num

def pull_energy(N):  # N is the money put in per month
	# amount to pull
	am_to_pull = N + random.randint(-10, 10)  # kWh
	return am_to_pull

def give_energy():
	return 

def cost():
	return 

def plotornot(cond, espend, ehow, es):
	if condition == 1:
		plt.figure()
		plt.bar(y_pos, espend, align = 'center', alpha = 0.5, color = 'g')
		plt.bar(y_pos, ehow, align = 'center', alpha = 0.5, color = 'b')
		plt.bar(y_pos, es, align = 'center', alpha = 0.5, color = 'r')
		plt.xlabel('house #')
		plt.ylabel('numerical value')
		plt.legend(('($)', 'kWh', '#people in a house'))
		plt.show()

##############################################################

how_many_houses = 10
num_reserves = 1

# Define $/kwh
USD_kWh = 1.27  # as USD_kWh increases, so does the amount that is stored in the tank

e = energy_usage()  # house
e.size = setup_houses(how_many_houses)

r = energy_reserve()
for j in range(num_reserves):
	for jj in range(len(e.size)):
		e.how_much.append(int(use_energy(e.size[jj])))
		e.spending.append(int(money_to_energy()))
	r.stored_energy.append(sum(e.spending)/USD_kWh)


print('num people per house: ', e.size)
print('energy: ', e.how_much, 'kWh')
print('money spent in a house: $', e.spending)
print('stored energy in reserve: ', r.stored_energy, 'kWh')

y_pos = np.arange(len(e.size))

# plot or don't plot. cause I don't want to plot this every time 
condition = 1
plotornot(condition, e.spending, e.how_much, e.size)


# Start a new loop, which does the pulling of energy, and the giving of energy
for j in range(len(e.size)):
	ee = pull_energy(e.how_much[j])
	r.stored_energy[0] -= ee

print('kWh left in reserve: ', r.stored_energy[0])


# Take energy from other houses
"Since each house has a percentage that they pay to the pool of $$ for the reserve, first take a percentage of what the $$ is to the pool for each house (factor), then multiply by how much to give back to the reserve, which should be negative"
if r.stored_energy[0] < 0:
	factor = 0
	factor_track = []
	num_give_back = 0
	for j in range(len(e.size)):
		factor = e.spending[j]/sum(e.spending)
		factor_track.append(factor)
		num_give_back += -r.stored_energy[0]*factor
		e.how_much[j] -= e.how_much[j]*factor
		# e.spending[j] += e.spending[j]*factor
	r.stored_energy[0] += num_give_back

	print(sum(factor_track))

	# If negative in the reserve, after the conditional for loop above, this number below should be 0
	print(r.stored_energy[0])



