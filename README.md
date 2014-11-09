mathia
======

My 2014-2015 IB Math HL Internal Assessment

Wikipedia network topography analysis, written in Python. No title yet.

Dataset thanks to [Henry Haselgrove](http://haselgrove.id.au/wikipedia.htm)––you can get it at that link. I include `links-simple-sorted.txt` and `titles-sorted.txt` in the same directory as my scripts; code refers to relative positions in several places, so leave them there.

## File index

+ `analysis.py` compiles the network into a list format and isolates the nodes for which it is possible to calculate a clustering coefficient (those with one link are ignored, and are very often redirect aliases anyway). It then calls functions defined in `localized_analysis.py` to evaluate those nodes. Currently, it calculates the clustering coefficient for every hundredth node.
+ `listmake.py` isn't actually commonly used, but may be used to pickle the links data once and for all. For now, just includes the stock data-to-list code that I'm copying and pasting everywhere because fisi
+ `localized_analysis.py` defines analysis at the micro level. Currently it includes several functions...
    + `clCoeff(oNode, finallist)` calculates the clustering coefficient for a given node. Currently it considers redirect alias nodes a part of the calculation, though perhaps at some point they should be excluded from 'finallist' somehow.
    + `getName(oNode)` gets the name of a node with ID `oNode` by pulling it from titles-sorted.txt.
    + `getOutlinks(oNode, finallist)` finds the outgoing links of a node with ID `oNode`. It returns `[dNode, namesList]`, where `dNode` is a list of numeric node indices to which the input node links, and where `namesList` is a list of strings for those nodes in the same order.


## To do list

+ Debug clustering coefficient calculation; returns values greater than 1, which should be maximum value. Current thought: some edges will be counted twice if two neighbors both link to the other, but not all edges will be counted twice (the link does not report inlinks).
+ Parallel processing! This may not be an issue––maybe just look at a portion (every hundredth node?) in the dataset?
