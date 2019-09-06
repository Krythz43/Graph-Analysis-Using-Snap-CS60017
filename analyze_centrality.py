import sys
import snap
import time

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

print "Initialting Calculations of Closeness Centrality using inbuilt function"
time.sleep(2)

closeness_centralities = []

for NI in G.Nodes():
    CloseCentr = snap.GetClosenessCentr(G, NI.GetId())
    print "node: %d centrality: %f" % (NI.GetId(), CloseCentr)
    closeness_centralities.append([CloseCentr,NI.GetId()])

closeness_centralities.sort(reverse=True)

print "The top 10 nodes are "
counter = 1

for X in closeness_centralities:
    if counter == 11:
        break
    print counter,X[1],X[0]
    counter = counter + 1

print "Inbuilt function for calculating Closeness centrality complete"
time.sleep(2)





# print "Initialting Calculations of Betweeness Centrality using inbuilt function"

# Nodes = snap.TIntFltH()
# Edges = snap.TIntPrFltH()
# snap.GetBetweennessCentr(G, Nodes, Edges, 0.8)
# for node in Nodes:
#     print "node: %d centrality: %f" % (node, Nodes[node])