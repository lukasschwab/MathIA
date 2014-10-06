import linecache, sys, random
from unidecode import unidecode

# I want a -l command to give the information on all the nodes involved
# Otherwise, just the numbers resulting from analysis

# Randomly select a node
lineno = random.randint(1,5706070)

# Gather its info
linestr = linecache.getline('links-simple-sorted.txt',lineno)
[origin, dest] = linestr.split(':')
dest = dest[1:-1]
dest = dest.split(' ')
dest[:] = [int(x) for x in dest]

# Gather the same info for each of the neighbors
# Indexed by twoSteps[neighborIndex1][neigborIndex2]
twoSteps = [None] * len(dest)
counter = 0
for neighbor in dest:
	linestr = linecache.getline('links-simple-sorted.txt',lineno)
	[waste, nOut] = linestr.split(':')
	nOut = nOut[1:-1]
	nOut = nOut.split(' ')
	nOut[:] = [int(x) for x in nOut]
	twoSteps[counter] = nOut
	counter+=1

print 'Node analyzed: ' + origin
print 'Connectivity: ' + str(len(dest))

# CLUSTERING COEFFICIENT
ai = len(dest)
Ei = float(0)
# Nested loop to be able to check links between neighbors
for x in twoSteps:
	tris = list(set(x) & set(dest)) # Network triangles
	Ei += len(tris)
# Calculate the coefficient
clCoeff = (2*Ei)/(ai*(ai-1))
print 'Clustering Coefficient: ' + str(clCoeff)