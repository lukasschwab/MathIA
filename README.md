mathia
======

My 2014-2015 IB Math HL Internal Assessment

Wikipedia network topography analysis, written in Python. No title yet.

Dataset thanks to [Henry Haselgrove](http://haselgrove.id.au/wikipedia.htm)––you can get it at that link. I include `links-simple-sorted.txt` and `titles-sorted.txt` in the same directory as my scripts; code refers to relative positions in several places, so leave them there.

## File index

+ *analysis.py* does big-scale analysis of the network (limited link-counting capability right now)
+ *listmake.py* isn't actually commonly used, but may be used to pickle the links data once and for all. For now, just includes the stock data-to-list code that I'm copying and pasting everywhere because fisi
+ *localized-analysis.py* does analysis on a randomly selected node, including the calculation of the clustering coefficient.


## To do list

+ Debug clustering coefficient calculation; returns values greater than 1, which should be maximum value.
+ Add large-scale clustering coefficient (list, average) to analysis.py