#
# soc-Epinions1-subgraph - out-degree Distribution. G(27407, 102004). 4297 (0.1568) nodes with out-deg > avg deg (7.4), 2639 (0.0963) with >2*avg.deg (Wed Sep  4 18:59:09 2019)
#

set title "soc-Epinions1-subgraph - out-degree Distribution. G(27407, 102004). 4297 (0.1568) nodes with out-deg > avg deg (7.4), 2639 (0.0963) with >2*avg.deg"
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
set output 'outDeg.soc-Epinions1-subgraph.png'
plot 	"outDeg.soc-Epinions1-subgraph.tab" using 1:2 title "" with linespoints pt 6
