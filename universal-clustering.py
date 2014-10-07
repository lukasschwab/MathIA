import linecache, sys, random
from unidecode import unidecode
import networkx as nx

# This is broken -- I don't have the memory to manage it

totalNetwork = nx.Graph()

# Gather its info
for lineno in range(1,5706071):
  linestr = linecache.getline('links-simple-sorted.txt',lineno)
  [origin, dest] = linestr.split(':')
  dest = dest[1:-1]
  dest = dest.split(' ')
  dest[:] = [int(x) for x in dest]
  for linkto in dest:
    totalNetwork.add_edge(origin, linkto)
  # Progress feedback
  print 'at ' + str(lineno) + ': ' + str(nx.average_clustering(totalNetwork))
