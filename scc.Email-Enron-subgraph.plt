#
# Email-Enron-subgraph - scc distribution. G(7275, 18453). Largest component has 0.836701 nodes (Sat Sep  7 20:38:07 2019)
#

set title "Email-Enron-subgraph - scc distribution. G(7275, 18453). Largest component has 0.836701 nodes"
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
set output 'scc.Email-Enron-subgraph.png'
plot 	"scc.Email-Enron-subgraph.tab" using 1:2 title "" with linespoints pt 6
