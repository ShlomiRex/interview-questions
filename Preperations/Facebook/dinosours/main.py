"""

You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.

$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.4,herbivore
Struthiomimus,0.72,omnivore
Velociraptor,1.8,carnivore
Triceratops,0.47,herbivore
Euoplocephalus,2.6,herbivore
Stegosaurus,1.50,herbivore
Tyrannosaurus Rex,6.5,carnivore

$ cat dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.97,quadrupedal
Stegosaurus,1.70,quadrupedal
Tyrannosaurus Rex,4.76,bipedal
Hadrosaurus,1.3,bipedal
Deinonychus,1.11,bipedal
Struthiomimus,1.24,bipedal
Velociraptorr,2.62,bipedal

"""

"""
Struthiomimus,1.91845
Velociraptorr,1.91333
Stegosaurus,0.511208
Hadrosaurus,-0.264575
Euoplocephalus,-1.22311
Tyrannosaurus Rex,-2.13651
"""

import math
from heapq import heapify, heappush, heappop

GRAVITY = 9.8

def calcSpeed(strideLen, legLen):
	return ((strideLen / legLen) - 1) * math.sqrt((legLen * GRAVITY))

def solution():
	bipedal_dino_hashmap = {}

	minheap = []
	heapify(minheap)

	# Read CSV2, store to dict if dinosaur is bipedal
	with open("dataset2.csv", "r") as csv2:
		lines = csv2.readlines()
		lines = lines[1:]
		for line in lines:
			columns = line.split(',')
			name = columns[0]
			stride_len = columns[1]
			stance = columns[2].strip()
			if stance == "bipedal":
				bipedal_dino_hashmap[name] = float(stride_len)

	# Read CSV1
	speed_and_bipedal_dino_name_hashmap = {}
	with open("dataset1.csv", "r") as csv1:
		lines = csv1.readlines()
		lines = lines[1:]
		for line in lines:
			columns = line.split(',')
			name = columns[0]
			leg_length = float(columns[1])
			#diet = columns[2].strip()

			if name in bipedal_dino_hashmap:
				stride_len = bipedal_dino_hashmap[name]
				speed = calcSpeed(stride_len, leg_length)
				# Push to min haep
				heappush(minheap, speed)
				# Push to hashmap, so we can later extract the name of the dino from the sorted speeds
				speed_and_bipedal_dino_name_hashmap[speed] = name

	# Extract from min heap the sorted speeds
	while minheap:
		speed = heappop(minheap)
		# Get name from speed
		name = speed_and_bipedal_dino_name_hashmap[speed]
		print(name, speed)

if __name__ == "__main__":
	res = calcSpeed(1.24, 0.72)
	res = round(res, 5)
	assert res == 1.91845

	solution()

