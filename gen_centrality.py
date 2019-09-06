import sys
import snap
import time
import sqlite3


#Setting Snap Randomized Seed Value to 42 

Rnd = snap.TRnd(42)
Rnd.Randomize()

if len(sys.argv) != 2 :
    print "[ERROR: INCORRECT ARGUMENTS] You need to pass exactly one argument which is the name of the edge list graph file stored in subgraphs folder."
    exit()

GName=sys.argv[1]
path="subgraphs/"+GName

try:
    G=snap.LoadEdgeList(snap.PUNGraph,path,0,1)
except:
    print "[ERROR: GRAPH NOT FOUND] Please check the graph file name and try again. Ensure the edge list is stored in subgraphs folder"
    exit()

nodes = G.GetNodes()
edges = G.GetEdges()


# Degree Centrality

# for NI in G.Nodes():
#     print "node: %d Degree Centrality: %d" % (NI.GetId(), NI.GetOutDeg())

# closeness centrality

counter =0

closeness_centralities = []

for NI in G.Nodes():
    NIdToDistH = snap.TIntH()
    sum_of_shortest_paths = 0

    shortestPath = snap.GetShortPath(G, NI.GetId(), NIdToDistH)

    for paths in NIdToDistH:
        sum_of_shortest_paths = sum_of_shortest_paths + NIdToDistH[paths]

    sum_of_shortest_paths = sum_of_shortest_paths + nodes*(nodes - len(NIdToDistH)) #incorporating unreachable nodes
    current_centrality=float(nodes)/sum_of_shortest_paths
    closeness_centralities.append([current_centrality,NI.GetId()])

    print NI.GetId(), " centrality = ",current_centrality, "nodes left = ",nodes-counter
    counter = counter + 1

closeness_centralities.sort(reverse=True)

print "The top 10 nodes are "
counter = 1

for X in closeness_centralities:
    if counter == 11:
        break
    print counter,X[1],X[0]
    counter = counter + 1



