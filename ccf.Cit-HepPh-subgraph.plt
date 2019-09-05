#
# Cit-HepPh-subgraph - clustering coefficient. G(16608, 103954). Average clustering: 0.2616  OpenTriads: 2806109 (0.9490)  ClosedTriads: 150897 (0.0510) (Thu Sep  5 22:20:40 2019)
#

set title "Cit-HepPh-subgraph - clustering coefficient. G(16608, 103954). Average clustering: 0.2616  OpenTriads: 2806109 (0.9490)  ClosedTriads: 150897 (0.0510)"
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
set output 'ccf.Cit-HepPh-subgraph.png'
plot 	"ccf.Cit-HepPh-subgraph.tab" using 1:2 title "" with linespoints pt 6
