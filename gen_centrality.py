import sys
import snap
import time
from collections import deque


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

# counter =0

# closeness_centralities = []

# for NI in G.Nodes():
#     NIdToDistH = snap.TIntH()
#     sum_of_shortest_paths = 0

#     shortestPath = snap.GetShortPath(G, NI.GetId(), NIdToDistH)

#     for paths in NIdToDistH:
#         sum_of_shortest_paths = sum_of_shortest_paths + NIdToDistH[paths]

#     sum_of_shortest_paths = sum_of_shortest_paths + nodes*(nodes - len(NIdToDistH)) #incorporating unreachable nodes
#     current_centrality=float(nodes)/sum_of_shortest_paths
#     closeness_centralities.append([current_centrality,NI.GetId()])

#     print NI.GetId(), " centrality = ",current_centrality, "nodes left = ",nodes-counter
#     counter = counter + 1

# closeness_centralities.sort(reverse=True)

# print "The top 10 nodes are "
# counter = 1

# for X in closeness_centralities:
#     if counter == 11:
#         break
#     print counter,X[1],X[0]
#     counter = counter + 1

Nodes = []

for NI in G.Nodes():
    Nodes.append(NI.GetId())

Adj = dict((v,[]) for v in Nodes)

for EI in G.Edges():
    u = EI.GetSrcNId()
    v = EI.GetDstNId()

    Adj[u].append(v)
    Adj[v].append(u)

C = dict((v,0.00) for v in Nodes)
    

counter = 0
start_time = time.time()

for s in Nodes:
    print "Nodes left = ",nodes-counter," time elapsed = ",time.time() - start_time

    S = []
    P = dict((w,[]) for w in Nodes)
    g = dict((t, 0) for t in Nodes); g[s] = 1
    d = dict((t,-1) for t in Nodes); d[s] = 0

    Q = deque([])
    Q.append(s)
    
    while Q:
        v = Q.popleft()
        S.append(v)
        for w in Adj[v]:
            if d[w] < 0:
                Q.append(w)
                d[w] = d[v] + 1
            if d[w] == d[v] + 1:
                g[w] = g[w] + g[v]
                P[w].append(v)
    e = dict((v, 0) for v in Nodes)
    while S:
        w = S.pop()
        for v in P[w]:
            e[v] = e[v] + float(g[v]/g[w]) * (1 + e[w])
        if w != s:
            C[w] = C[w] + e[w]

    counter = counter + 1

# print C

betweeness_centrality = []

for Node in Nodes:
    betweeness_centrality.append([C[Node],Node])

betweeness_centrality.sort(reverse=True)


time_taken = time.time() - start_time

print "Execution for betweeness centrality completed in ",time_taken//60," mins and ",(time_taken//1)%60, "seconds"
print "The top 10 nodes are:"
counter = 1

for X in betweeness_centrality:
    if counter == 11:
        break
    print counter,X[1],X[0]
    counter = counter + 1




