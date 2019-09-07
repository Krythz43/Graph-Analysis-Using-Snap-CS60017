import sys
import snap
import time






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



def calculate_degree_centrality(G,GName,Nodes,nodes,edges):
    
    print "Initialting Calculations of Degree using inbuilt function"
    
    start_time = time.time()

    closeness_centralities = []

    for NI in G.Nodes():
        CloseCentr = snap.GetClosenessCentr(G, NI.GetId())
        closeness_centralities.append([CloseCentr,NI.GetId()])

    closeness_centralities.sort(reverse=True)

    time_taken = time.time() - start_time
    print "Execution for Cetweeness Centrality completed in ",time_taken//60," mins and ",(time_taken//1)%60, "seconds"

    return closeness_centralities








def calculate_closeness_centrality(G,GName,Nodes,nodes,edges):

    print "Initialting Calculations of Closeness Centrality using inbuilt function"
    
    start_time = time.time()

    closeness_centralities = []

    for NI in G.Nodes():
        CloseCentr = snap.GetClosenessCentr(G, NI.GetId())
        closeness_centralities.append([CloseCentr,NI.GetId()])

    closeness_centralities.sort(reverse=True)

    time_taken = time.time() - start_time
    print "Execution for Closeness Centrality completed in ",time_taken//60," mins and ",(time_taken//1)%60, "seconds"

    return closeness_centralities







def calculate_betweeness_centrality(G,GName,Nodes,nodes,edges):

    print "Initialting Calculations of Betweeness Centrality using inbuilt function"
    start_time = time.time()

    Nodes = snap.TIntFltH()
    Edges = snap.TIntPrFltH()
    snap.GetBetweennessCentr(G, Nodes, Edges, 0.8)

    # for node in Nodes:
    #     print "node: %d centrality: %f" % (node, Nodes[node])


    betweeness_centralities = []

    for Node in Nodes:
        betweeness_centralities.append([Nodes[Node],Node])

    betweeness_centralities.sort(reverse=True)
    time_taken = time.time() - start_time
    print "Execution for Betweeness Centrality completed in ",time_taken//60," mins and ",(time_taken//1)%60, "seconds"

    return betweeness_centralities







def get_top_10(arg_list):

    return arg_list[:10]








def print_values(method_name, arg_list):
    print "The top ",len(arg_list)," nodes of ",method_name," are:"

    for i in range(len(arg_list)):
        print "{0} \t node = {1} \t  centrality = {2}".format(i+1,arg_list[i][1],arg_list[i][0])


def get_values_to_be_compared_with():
    
    closeness_centralities = [195,444,273,78,516,423,639,588,1077,378]
    betweeness_centralities = [273,588,195,543,516,1824,4746,444,213,5022]

    return closeness_centralities,betweeness_centralities



def compare_top_10(centrality_type,calculated_values,generated_values_with_inbuilt):

    number_of_overlaps = 0

    generated_values = []
    for X in generated_values_with_inbuilt:
        generated_values.append(X[1])

    for NI in calculated_values:
        if NI in generated_values:
            number_of_overlaps = number_of_overlaps + 1

    print "Number of overlaps for {0}: {1}".format(centrality_type,number_of_overlaps)





if __name__ == "__main__":

    #Setting Snap Randomized Seed Value to 42 
    Rnd = snap.TRnd(42)
    Rnd.Randomize()

    G,GName,Nodes,nodes,edges = fetch_graph()

    closeness_centralities = calculate_closeness_centrality(G,GName,Nodes,nodes,edges)
    betweeness_centralities = calculate_betweeness_centrality(G,GName,Nodes,nodes,edges)

    closeness_top10 = get_top_10(closeness_centralities)
    betweeness_top10 = get_top_10(betweeness_centralities)

    print_values("Closeness Centraliry" , closeness_top10)
    print_values("Betweeness Centrality" , betweeness_top10)

    closeness_calculated_values,betweeness_calculated_values = get_values_to_be_compared_with()

    compare_top_10("Closeness Centrality",closeness_calculated_values,closeness_top10)
    compare_top_10("Betweeness Centrality",betweeness_calculated_values,betweeness_top10)
