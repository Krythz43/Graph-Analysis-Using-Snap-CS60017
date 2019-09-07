import sys
import snap
import time
from collections import deque





def fetch_graph():

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

    Nodes = []

    for NI in G.Nodes():
        Nodes.append(NI.GetId())

    return G,GName,Nodes,nodes,edges








def store_in_file(arg_list,file_name,GName):

    path = GName[:-10]+"_"+file_name+".txt"
    file = open(path,'w')

    for X in arg_list:
        file.write(str(X[1])+" "+str(X[0])+"\n")

    print "File created for storing " + GName[:-10] + " with the name " + path

    file.close()







def compute_degree_centrality(G,GName):

    degree_centrality = []

    for NI in G.Nodes():
        degree_centrality.append([NI.GetOutDeg(),NI.GetId()])
    
    degree_centrality.sort()

    store_in_file(degree_centrality,"degree_centrality",GName)







def compute_closeness_centrality(G,GName,Nodes,nodes,edges):

    counter =0
    closeness_centralities = []

    start_time = time.time()

    for NI in G.Nodes():
        NIdToDistH = snap.TIntH()
        sum_of_shortest_paths = 0
        shortestPath = snap.GetShortPath(G, NI.GetId(), NIdToDistH)

        for paths in NIdToDistH:
            sum_of_shortest_paths = sum_of_shortest_paths + NIdToDistH[paths]

        sum_of_shortest_paths = sum_of_shortest_paths + nodes*(nodes - len(NIdToDistH)) #incorporating unreachable nodes
        current_centrality=float(nodes)/sum_of_shortest_paths
        closeness_centralities.append([current_centrality,NI.GetId()])

    time_taken = time.time() - start_time
    print "Execution for Closeness Centrality completed in ",time_taken//60," mins and ",(time_taken//1)%60, "seconds"
    
    closeness_centralities.sort()
    store_in_file(closeness_centralities,"closeness_centrality",GName)
    closeness_centralities.sort(reverse=True)

    return closeness_centralities










def compute_betweeness_centrality(G,GName,Nodes,nodes,edges):

    Adj = dict((v,[]) for v in Nodes)

    for EI in G.Edges():
        u = EI.GetSrcNId()
        v = EI.GetDstNId()

        Adj[u].append(v)
        Adj[v].append(u)

    C = dict((v,0.00) for v in Nodes)


    start_time = time.time()

    for s in Nodes:

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

    time_taken = time.time() - start_time
    print "Execution for Betweeness Centrality completed in ",time_taken//60," mins and ",(time_taken//1)%60, "seconds"


    betweeness_centralities = []

    for Node in Nodes:
        betweeness_centralities.append([C[Node],Node])

    betweeness_centralities.sort()
    store_in_file(betweeness_centralities,"betweeness_centrality",GName)
    betweeness_centralities.sort(reverse=True)


    time_taken = time.time() - start_time

    return betweeness_centralities




def get_top_10(arg_list):
    
    return arg_list[:10]








def print_values(method_name, arg_list):
    print "The top ",len(arg_list)," nodes of ",method_name," are:"

    for i in range(len(arg_list)):
        print "{0} \t node = {1} \t  centrality = {2}".format(i+1,arg_list[i][1],arg_list[i][0])




if __name__ == "__main__":

    #Setting Snap Randomized Seed Value to 42 
    Rnd = snap.TRnd(42)
    Rnd.Randomize()

    G,GName,Nodes,nodes,edges = fetch_graph()
    compute_degree_centrality(G,GName)
    closeness_centralities = compute_closeness_centrality(G,GName,Nodes,nodes,edges)
    betweeness_centralities = compute_betweeness_centrality(G,GName,Nodes,nodes,edges)

    closeness_top10 = get_top_10(closeness_centralities)
    betweeness_top10 = get_top_10(betweeness_centralities)

    print_values("Closeness Centraliry" , closeness_top10)
    print_values("Betweeness Centrality" , betweeness_top10)
    

    




