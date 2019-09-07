#
# Email-Enron-subgraph - clustering coefficient. G(7275, 18453). Average clustering: 0.2884  OpenTriads: 713482 (0.9685)  ClosedTriads: 23202 (0.0315) (Sat Sep  7 20:38:08 2019)
#

set title "Email-Enron-subgraph - clustering coefficient. G(7275, 18453). Average clustering: 0.2884  OpenTriads: 713482 (0.9685)  ClosedTriads: 23202 (0.0315)"
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
set output 'ccf.Email-Enron-subgraph.png'
plot 	"ccf.Email-Enron-subgraph.tab" using 1:2 title "" with linespoints pt 6
