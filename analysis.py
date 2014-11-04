import random
import linecache
from unidecode import unidecode

# Process links into list
finallist = [None] * 5716809
with open('links-simple-sorted.txt', 'r') as src:
	for line in src:
		[oNode, dNode] = line.split(':')
		finallist[int(oNode)] = dNode.rstrip('\n')[1:]

# ACTUALLY: pick a random line in links-sorted, and translate the numbers from there

# Get a random node, and pull that line from the links doc; want this to be an option

oNode = random.randint(1,5706070)
dNode = finallist[oNode]
dNode = dNode.split(' ')

# Translate these into titles and print the result
oname = linecache.getline('titles-sorted.txt',int(oNode))
oname = oname[:-1] # Gets rid of the trailing newline
print '\nORIGIN NODE: ' + oname + '\n'

print 'DESTINATION NODES:'
for thisnum in dNode:
	dname = linecache.getline('titles-sorted.txt',int(thisnum))[:-1]
	print '     ' + dname
print '\n'