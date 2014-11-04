# Creates list finallist
# For index i
# finallist[i] is the links out, in the form of a string separated by spaces:
# 	finallist[2] = '3 747213 1664968 1691047 4095634 5535664'

finallist = [None] * 5716809

with open('links-simple-sorted.txt', 'r') as src:
	for line in src:
		[oNode, dNode] = line.split(':')
		finallist[int(oNode)] = dNode.rstrip('\n')[1:]
print 'What is finallist[0]?'
print finallist[0:3]