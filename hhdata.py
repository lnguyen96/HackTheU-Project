import random

filename = 'hhSizeAndName.csv'

f = open(filename, 'w')
headers = 'Household Size, Household Name\n'
f.write(headers)

#n = input('Enter # of houses:')

#n = int(n)

n = 50

for i in range(n):
	hhSize = str(random.randint(1,8))
	hhName = 'h' + str(i)
	#print(hhSize,hhName)
	f.write(hhSize + ',' + hhName + '\n')

f.close()
