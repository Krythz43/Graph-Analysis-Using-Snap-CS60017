#
# p2p-Gnutella04-subgraph - out-degree Distribution. G(10876, 39994). 4554 (0.4187) nodes with out-deg > avg deg (7.4), 1339 (0.1231) with >2*avg.deg (Fri Sep  6 19:15:41 2019)
#

set title "p2p-Gnutella04-subgraph - out-degree Distribution. G(10876, 39994). 4554 (0.4187) nodes with out-deg > avg deg (7.4), 1339 (0.1231) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Out-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'outDeg.p2p-Gnutella04-subgraph.png'
plot 	"outDeg.p2p-Gnutella04-subgraph.tab" using 1:2 title "" with linespoints pt 6
