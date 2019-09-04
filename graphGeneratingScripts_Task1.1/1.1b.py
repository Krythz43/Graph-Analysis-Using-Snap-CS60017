import snap

G1=snap.LoadEdgeList(snap.PUNGraph,"../subgraphs/Cit-HepPh.txt",0,1)
G2=snap.TUNGraph.New()

for NI in G1.Nodes():
    if NI.GetId()%2 == 0 :
        G2.AddNode(NI.GetId())

for EI in G1.Edges():
    if EI.GetSrcNId()%2 == 0 and EI.GetDstNId()%2 == 0 :
        G2.AddEdge(EI.GetSrcNId(),EI.GetDstNId())

print snap.GetClustCf(G2)
print G2.GetNodes()

snap.SaveEdgeList(G2, "../subgraphs/Cit-HepPh-subgraph.elist.txt", "List of edges")

