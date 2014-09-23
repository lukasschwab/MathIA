import linecache, pickle, sys
links = [None] * 5706070
adjMatrix = []
for lineno in range(1,5706070):
	linestr = linecache.getline('links-simple-sorted.txt',lineno)
	[origin, dest] = linestr.split(':')
	dest = dest[1:-1]
	dest = dest.split(' ')
	dest[:] = [int(x) for x in dest]
	links[lineno-1] = dest
	

	# There is something broke a f about this bit
	for x in dest:
		linksout = [0]*5706070
		if x <= 5706070:
			linksout[x]=1
	adjMatrix.append(linksout)
	print lineno # Progress feedback

# How to open the file here?
pickle.dump(links, open("links","wb"))
pickle.dump(adjMatrix, open("adjMatrix","wb"))

sys.exit()