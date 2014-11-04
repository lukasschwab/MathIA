import linecache, sys, random
from unidecode import unidecode

# I want a -l command to give the information on all the nodes involved
# Otherwise, just the numbers resulting from analysis

# Gather its info
finallist = [None] * 5716809
with open('links-simple-sorted.txt', 'r') as src:
	for line in src:
		[oNode, dNode] = line.split(':')
		finallist[int(oNode)] = dNode.rstrip('\n')[1:]

# Randomly select a node
oNode = random.randint(1,5716809)
oname = linecache.getline('titles-sorted.txt',int(oNode))
dNode = finallist[oNode].split(' ')

# Gather the same info for each of the neighbors
# Make this a function, can do recursive calls to check multiple depths?
twoSteps = ''
for neighbor in dNode:
	twoSteps += finallist[int(neighbor)]
twoSteps = twoSteps.split(' ')

# Have to find the number of overlaps
oneANDtwo = 0
for firstStep in dNode:
	oneANDtwo += twoSteps.count(firstStep)

print ''
print 'Node analyzed: ' + str(oNode) + ': ' + oname[:-1]
print 'Connectivity: ' + str(len(dNode))
print 'Two-step connectivity: ' + str(len(twoSteps))


if len(dNode) > 1:
	# CLUSTERING COEFFICIENT
	ai = float(len(dNode))
	Ei = float(oneANDtwo)
	# Calculate the coefficient
	clCoeff = (2*Ei)/(ai*(ai-1))
	print 'Clustering Coefficient: ' + str(clCoeff)

print ''