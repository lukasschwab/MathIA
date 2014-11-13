import random
import linecache
from unidecode import unidecode
from localized_analysis import clCoeff
from statistics import mode, mean

# Process links into list
notredirects = []
finallist = [None] * 5716809
with open('links-simple-sorted.txt', 'r') as src:
	for line in src:
		[oNode, dNode] = line.split(':')
		if len(dNode.rstrip('\n').split(' ')) > 2:
			notredirects += [int(oNode)]
		finallist[int(oNode)] = dNode.rstrip('\n')[1:]

clCoeffs = []
node = 1
while node <= len(notredirects):
	clCoeffs += [clCoeff(int(node), finallist)]
	node += 100

print 'AVERAGE: ' + str(float(sum(clCoeffs)/len(clCoeffs)))
print 'MINIMUM: ' + str(min(list))
print 'MAXIMUM: ' + str(max(list))
print 'MODE:    '