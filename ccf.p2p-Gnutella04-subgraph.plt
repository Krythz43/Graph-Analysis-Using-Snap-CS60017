#
# p2p-Gnutella04-subgraph - clustering coefficient. G(10876, 39994). Average clustering: 0.0062  OpenTriads: 515892 (0.9982)  ClosedTriads: 934 (0.0018) (Sat Sep  7 20:38:48 2019)
#

set title "p2p-Gnutella04-subgraph - clustering coefficient. G(10876, 39994). Average clustering: 0.0062  OpenTriads: 515892 (0.9982)  ClosedTriads: 934 (0.0018)"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Node degree"
set ylabel "Average clustering coefficient"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'ccf.p2p-Gnutella04-subgraph.png'
plot 	"ccf.p2p-Gnutella04-subgraph.tab" using 1:2 title "" with linespoints pt 6
