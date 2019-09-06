#
# p2p-Gnutella04-subgraph - scc distribution. G(10876, 39994). Largest component has 1.000000 nodes (Fri Sep  6 19:15:41 2019)
#

set title "p2p-Gnutella04-subgraph - scc distribution. G(10876, 39994). Largest component has 1.000000 nodes"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Size of strongly connected component"
set ylabel "Number of components"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'scc.p2p-Gnutella04-subgraph.png'
plot 	"scc.p2p-Gnutella04-subgraph.tab" using 1:2 title "" with linespoints pt 6
