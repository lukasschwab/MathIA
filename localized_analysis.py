import linecache, sys, random
from unidecode import unidecode

def clCoeff(oNode, finallist):
	oname = linecache.getline('titles-sorted.txt',int(oNode))
	if type(finallist[oNode]) != type(None):
		dNode = finallist[oNode].split(' ')

	# Gather the same info for each of the neighbors
	# Make this a function, can do recursive calls to check multiple depths?
	twoSteps = ''
	for neighbor in dNode:
		if len(neighbor) > 0 and type(finallist[int(neighbor)]) != type(None):
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
		# Links are often (not always) counted twice...
		clCoeff = (2*Ei)/(ai*(ai-1))
		return clCoeff
	else:
		return 0