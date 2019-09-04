import sys
import snap

if len(sys.argv) != 2 :
    print "[ERROR: INCORRECT ARGUMENTS] You need to pass exactly one argument which is the name of the edge list graph file stored in subgraphs folder."
    exit()

GName=sys.argv[1]
path="subgraphs/"+GName

try:
    G=snap.LoadEdgeList(snap.PUNGraph,path,0,1)
except:
    print "[ERROR: GRAPH NOT FOUND] Please check the graph file name and try again. Ensure the edge list is stored in subgraphs folder"

degree = G.GetNodes()
edges = G.GetEdges()

print "Number of nodes in {0}: {1}".format(GName[:-10],degree)
print "Number of edges in {0}: {1}".format(GName[:-10],edges)


CntV=snap.TIntPrV()

snap.GetOutDegCnt(G,CntV) 
flag = 0
for p in CntV:
    if p.GetVal1() == 7:
        flag = p.GetVal2()
        break

print "Number of nodes with degree=7 in %s: %d" % (GName[:-10], flag)

MaxDegree=CntV[len(CntV)-1].GetVal1()
# print MaxDegree

Nodes_with_max_deg = []

for NI in G.Nodes():
    if NI.GetOutDeg() == MaxDegree:
        Nodes_with_max_deg.append(str(NI.GetId()))

string_of_nodes_with_max_deg=",".join(Nodes_with_max_deg)

print "Node id (s) with highest degree in {0}: {1}".format(GName[:-10],string_of_nodes_with_max_deg)

filename="outDeg."+GName[:-10]+".png"
snap.PlotOutDegDistr(G, GName[:-10], GName[:-10] + " - out-degree Distribution")
print "Degree distribution of {0} is in: {1}".format(GName[:-10],filename)



