import random
import linecache
from unidecode import unidecode

# ACTUALLY: pick a random line in links-sorted, and translate the numbers from there

# Get a random node, and pull that line from the links doc––want this to be an option
# Pull from links because some titles don't have link lines
lineno = random.randint(1,5706070)

linestr = linecache.getline('links-simple-sorted.txt',lineno)

# Process the string to split the "from" and "to" numbers
[origin, dest] = linestr.split(':')
dest = dest[1:-1] # Gets rid of the first space and trailing newline
dest = dest.split(' ') # Split at spaces

# Translate these into title
oname = lincache.getline('titles-sorted.txt',int(origin))
oname = oname[:-1] # Gets rid of the trailing newline
UNIoname = unidecode(u oname)

for thisnum in dest:
	dname = linecache.getline('titles-sorted.txt',int(thisnum))[:-1]
	UNIdname = unidecode(linecache.getline('titles-sorted.txt', int(thisnum))[:-1])

# Get some stats bro
linksout = len(dest)
# To get linksin need an adjacency matrix

def assemblematrix():
	# Something with links-simple-sorted.txt
	# Parse that shit in

def linksin(node):
	# Locations of value "1" in the row int(node)

def linksout(node):
	# Locations of value "1" in the col int(node)

