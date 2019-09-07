#
# Email-Enron-subgraph - out-degree Distribution. G(7275, 18453). 1252 (0.1721) nodes with out-deg > avg deg (5.1), 683 (0.0939) with >2*avg.deg (Sat Sep  7 20:38:07 2019)
#

set title "Email-Enron-subgraph - out-degree Distribution. G(7275, 18453). 1252 (0.1721) nodes with out-deg > avg deg (5.1), 683 (0.0939) with >2*avg.deg"
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
set output 'outDeg.Email-Enron-subgraph.png'
plot 	"outDeg.Email-Enron-subgraph.tab" using 1:2 title "" with linespoints pt 6
