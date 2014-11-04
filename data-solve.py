
with open('links-simple-sorted.txt', 'r') as src:
	with open('links-data-improved.txt', 'w') as dest:
		lineno = 1
		noCorrected = 0
		for line in src:
			[oNode, dNode] = line.split(':')
			if int(oNode) == (lineno + noCorrected):
				dest.write('%s\n' % (line.rstrip('\n')))
			else:
				dest.write('%s\n' % (str(lineno) + ': '))
				noCorrected += 1
			lineno += 1