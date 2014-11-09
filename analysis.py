import random
import linecache
from unidecode import unidecode
from localized_analysis import clCoeff

# Process links into list
notredirects = []
finallist = [None] * 5716809
with open('links-simple-sorted.txt', 'r') as src:
	for line in src:
		[oNode, dNode] = line.split(':')
		if len(dNode.rstrip('\n').split(' ')) > 2:
			notredirects += [int(oNode)]
		finallist[int(oNode)] = dNode.rstrip('\n')[1:]

node = 1
while node <= len(notredirects):
	test = clCoeff(int(node), finallist)
	print str(node) + ' / ' + str(len(notredirects)) + ':     ' + str(test)
	node += 100