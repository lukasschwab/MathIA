import random
import linecache
from unidecode import unidecode

# Process links into list
finallist = [None] * 5716809
with open('links-simple-sorted.txt', 'r') as src:
	for line in src:
		[oNode, dNode] = line.split(':')
		finallist[int(oNode)] = dNode.rstrip('\n')[1:]

##########################################################################################
# Analyze basic properties of a particular node (randomly selected) 

# Get a random node, and pull that line from the links doc; want this to be an option
# oNode = random.randint(1,5706070)
# dNode = finallist[oNode]
# dNode = dNode.split(' ')
# Translate these into titles and print the result
# oname = linecache.getline('titles-sorted.txt',int(oNode))
# oname = oname[:-1] # Gets rid of the trailing newline
# print '\nORIGIN NODE: ' + oname + '\n'
# print 'DESTINATION NODES:'
# for thisnum in dNode:
# 	dname = linecache.getline('titles-sorted.txt',int(thisnum))[:-1]
# 	print '     ' + dname
# print '\n'

##########################################################################################
# Connectivity across the whole network

# Calculate average number of 1st-order connections
totalConn = 0
linksout = []
for node in finallist:
	if node != None: # If the oNode has outlinks
		totalConn += len(node.split(' '))
		linksout += [len(node.split(' '))]
	else:
		linksout += [0]
avgConn = float(totalConn/5716809)
print avgConn
print max(linksout)

##########################################################################################
# Average clustering coefficient

for oNode in range(1,5716809+1):
	oname = linecache.getline('titles-sorted.txt',int(oNode))
	dNode = finallist[oNode].split(' ')

	# Gather the same info for each of the neighbors
	# Make this a function, can do recursive calls to check multiple depths?
	twoSteps = ''
	for neighbor in dNode:
		if dNode != ['']:
			twoSteps += finallist[int(neighbor)]
	twoSteps = twoSteps.split(' ')

	# Have to find the number of overlaps
	oneANDtwo = 0
	for firstStep in dNode:
		oneANDtwo += twoSteps.count(firstStep)


	if len(dNode) > 1:
		# CLUSTERING COEFFICIENT
		ai = float(len(dNode))
		Ei = float(oneANDtwo)
		# Calculate the coefficient
		clCoeff = (2*Ei)/(ai*(ai-1))
		print 'Clustering Coefficient: ' + str(clCoeff)