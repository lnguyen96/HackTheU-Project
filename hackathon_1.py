"Niklaus Parcell, Deron parcell, Long Nguyen, Edwin Chiang"

"Personalized algorithm for cancer therapy with better financial strategy"

import numpy as np 
import random
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation 


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
		n_groups = 10
		index = np.arange(n_groups)
		bar_width = 0.3
		opacity = 0.8
		plt.figure()
		# plt.bar(y_pos, espend, align = 'center', alpha = 0.5, color = 'g')
		# plt.bar(y_pos, ehow, align = 'center', alpha = 0.5, color = 'b')
		# plt.bar(y_pos, es, align = 'center', alpha = 0.5, color = 'r')
		plt.bar(index, espend, bar_width, alpha = opacity, color = 'g', label='$')
		plt.bar(index + bar_width, ehow, bar_width, alpha = opacity, color = 'b', label = 'kWh')
		plt.bar(index + 2*bar_width, es, bar_width, alpha = opacity, color = 'r', label = '#people in a house')
		plt.xlabel('house #')
		plt.ylabel('numerical value')
		plt.legend(('($)', 'kWh', '#people in a house'))
		plt.tight_layout()
		plt.show()

def plot_grow(growth):

	for j in range(len(growth)):
		growth[j] *= 30
	# Create new figure and axes which fill it
	fig = plt.figure(figsize=(6,6))
	ax = fig.add_axes([0, 0, 1, 1], frameon = False)
	ax.set_xlim(-1.5, 1.5), ax.set_xticks([])
	ax.set_ylim(-1.5, 1.5), ax.set_yticks([])

	# Create "rain" data
	n_drops = 10
	rain_drops = np.zeros(n_drops, dtype = [('position', float, 2), ('size', float, 1), ('growth', float, 1), ('color', float, 4)])

	# Initialize raindrops in (non-random) positions and with random growth rates
	pos1 = (np.sqrt(3)/2, 1/2)
	pos2 = (1/2, np.sqrt(3)/2)
	pos3 = (0, 1)
	pos4 = (-1/2, np.sqrt(3)/2)
	pos5 = (-np.sqrt(3)/2, 1/2)
	pos6 = (-np.sqrt(3)/2, -1/2)
	pos7 = (-1/2, -np.sqrt(3)/2)
	pos8 = (0, -1)
	pos9 = (1/2, -np.sqrt(3)/2)
	pos10 = (np.sqrt(3)/2, -1/2)
	xs = [np.sqrt(3)/2, 1/2, 0, -1/2, -np.sqrt(3)/2, -np.sqrt(3)/2, -1/2, 0, 1/2, np.sqrt(3)/2]
	ys = [1/2, np.sqrt(3)/2, 1, np.sqrt(3)/2, 1/2, -1/2, -np.sqrt(3)/2, -1, -np.sqrt(3)/2, -1/2]
	positions = [xs, ys]
	for j in range(n_drops):
		rain_drops['position'][j] = (xs[j], ys[j])
	# print(rain_drops['position'])
	rain_drops['size'] = growth

	# Construct the 'scatter' of each 'drop'
	scat = ax.scatter(rain_drops['position'][:,0], rain_drops['position'][:,1], s = rain_drops['size'], lw = 0.5, edgecolors = rain_drops['color'], facecolors = 'none')

	def update(frame_number):
		# index to re-spawn 'oldest' raindrop
		curr_index = frame_number % n_drops

		# Change circle size
		rain_drops['size'] = growth

		# Re-position
		for j in range(n_drops):
			rain_drops['position'][j] = (xs[j], ys[j]) 
		rain_drops['size'][curr_index] = 1
		rain_drops['color'][curr_index] = (0, 0, 0, 1)
		rain_drops['growth'][curr_index] = 0

		# Update scatter collection
		scat.set_edgecolors(rain_drops['color'])
		# scat.set_sizes(rain_drops['size'])
		# scat.set_offsets(rain_drops['position'])

	animation = FuncAnimation(fig, update, interval = 200)
	plt.show()

##############################################################

how_many_houses = 10
num_reserves = 1

# Define $/kwh
USD_kWh = 1.27  # as USD_kWh increases, so does the amount that is stored in the tank

# Constructor
e = energy_usage()  # house


# print('num people per house: ', e.size)
# print('energy: ', e.how_much, 'kWh')
# print('money spent in a house: $', e.spending)
# print('stored energy in reserve: ', r.stored_energy, 'kWh')



# Start a new loop, which does the pulling of energy, and the giving of energy
e = energy_usage()
e.size = setup_houses(how_many_houses)
e_rem = e.size
r = energy_reserve()

num_months = 12

ee = np.zeros((num_months, how_many_houses))

for jjj in range(num_months):

	for j in range(num_reserves):
		for jj in range(len(e.size)):
			e.spending.append(int(money_to_energy()))
			e.how_much.append(int(use_energy(e.size[jj])))

		e_spend = e.spending	
	
		r.stored_energy.append(sum(e.spending)/USD_kWh)
		
	for j in range(len(e.size)):
		eee = pull_energy(e.how_much[j])
		ee[jjj][j] = eee
		r.stored_energy[0] -= eee

	# print('kWh left in reserve: ', r.stored_energy[0])

	# plot or don't plot. cause I don't want to plot this every time 
	condition = 1
	plotornot(condition, e.spending, e.how_much, e.size)

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
		# print(sum(factor_track))
		
		# If negative in the reserve, after the conditional for loop above, this number below should be 0
		# print(r.stored_energy[0])

	# reset vals
	e.how_much, e.spending = [], []

# Show plotted change over time (just doing one change of size)
plot_grow(ee[0])

