finallist = [None] * 5716809

with open('links-simple-sorted.txt', 'r') as src:
	for line in src:
		[oNode, dNode] = line.split(':')
		finallist[int(oNode)] = dNode.rstrip('\n')[1:]
print 'What is finallist[0]?'
print finallist[0:3]