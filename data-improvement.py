import linecache, sys
for lineno in range (1,5706071):
	linestr = linecache.getline('links-data-improved.txt', lineno)
	if len(linestr) < 2:
		print lineno
	else:
		[origin, dest] = linestr.split(':')
		if int(origin) != lineno:
			print lineno
			sys.exit()