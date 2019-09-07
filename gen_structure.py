import sys
import snap




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

    return  G,GName







def get_nodes_and_edges(G,GName):

    nodes = G.GetNodes()
    edges = G.GetEdges()

    print "Number of nodes in {0}: {1}".format(GName[:-10],nodes)
    print "Number of edges in {0}: {1}".format(GName[:-10],edges)

    return nodes,edges










def solve_degree_based_questions(G,GName):

    #Number of nodes with degre seven

    CntV=snap.TIntPrV()

    snap.GetOutDegCnt(G,CntV) 
    flag = 0
    for p in CntV:
        if p.GetVal1() == 7:
            flag = p.GetVal2()
            break

    print "Number of nodes with degree=7 in %s: %d" % (GName[:-10], flag)


    #To find the number of nodes with maximum degree and thier IDs
    MaxDegree=CntV[len(CntV)-1].GetVal1()
    Nodes_with_max_deg = []

    for NI in G.Nodes():
        if NI.GetOutDeg() == MaxDegree:
            Nodes_with_max_deg.append(str(NI.GetId()))

    string_of_nodes_with_max_deg=",".join(Nodes_with_max_deg)
    print "Node id (s) with highest degree in {0}: {1}".format(GName[:-10],string_of_nodes_with_max_deg)


    #Plots the Degree Distribution

    filename="outDeg."+GName[:-10]+".png"
    snap.PlotOutDegDistr(G, GName[:-10], GName[:-10] + " - out-degree Distribution")
    print "Degree distribution of {0} is in: {1}".format(GName[:-10],filename)










def solve_shortest_path_based_questions(G,GName):
    # 

    # effdiam1 = snap.GetBfsEffDiamAll(G, 10, False)
    # print diam1
    # effdiam2 = snap.GetBfsEffDiamAll(G, 100, False)
    # print diam2
    # effdiam3 = snap.GetBfsEffDiamAll(G, 1000, False)
    # print diam3


    # snap.PlotShortPathDistr(G, GName[:-10], GName[:-10]+" - shortest path")

    filename="diam."+GName[:-10]+".png"
    print "Shortest path distribution of {0} is in: {1}".format(GName[:-10],filename)








def fraction_of_nodes_in_largest_connected_component(G,GName):
    
    ComponentDist = snap.TIntPrV()
    snap.GetSccSzCnt(G, ComponentDist)
    highest_nodes_in_connected_comp=0
    
    for comp in ComponentDist:
        highest_nodes_in_connected_comp = max(comp.GetVal1(), highest_nodes_in_connected_comp)
    
    print "Fraction of nodes in largest connected component in {0}: {1}".format(GName[:-10],(float(str(highest_nodes_in_connected_comp))/G.GetNodes()))









def number_of_bridges(G,GName):
    
    EdgeV = snap.TIntPrV()
    snap.GetEdgeBridges(G, EdgeV)
    bridges_in_graph=len(EdgeV)
    
    print "Number of edge bridges in {0}: {1}".format(GName[:-10],bridges_in_graph)










def number_of_articulation_points(G,GName):
    
    ArtNIdV = snap.TIntV()
    snap.GetArtPoints(G, ArtNIdV)
    articulation_points_in_graph=len(ArtNIdV)
    
    print "Number of articulation points in {0}: {1}".format(GName[:-10],articulation_points_in_graph)









def plot_component_size_distribution(G,GName):
    
    snap.PlotSccDistr(G, GName[:-10], GName[:-10]+" - scc distribution")    
    filename="scc."+GName[:-10]+".png"
    
    print "Component size distribution of {0} is in: {1}".format(GName[:-10],filename)










def print_average_ccf_and_traid_count(G,GName):

    DegToCCfV = snap.TFltPrV()
    result = snap.GetClustCfAll(G, DegToCCfV)

    print "Average clustering coefficient in {0}: {1:.4f}".format(GName[:-10],result[0])
    print "Number of traids in {0}: {1}".format(GName[:-10],result[1])











def print_ccf_of_random_node(G,GName):
    
    NIdCCfH = snap.TIntFltH()
    snap.GetNodeClustCf(G, NIdCCfH)
    random_node_index=snap.TInt.GetRnd(len(NIdCCfH))

    counter = 0
    for item in NIdCCfH:
        if counter == random_node_index:
            print "Clustering coefficient of random node {0} in {1}: {2}".format(item,GName[:-10],NIdCCfH[item])
            break
        counter = counter + 1











def print_number_of_traids_participated_by_random_node(G,GName):

    TriadV = snap.TIntTrV()
    snap.GetTriads(G, TriadV)
    random_traid_node_index=snap.TInt.GetRnd(len(TriadV))
    counter = 0
    for triple in TriadV:   
        if counter == random_traid_node_index:
            print "Number of traids of random node {0} participates in {1}: {2}".format(triple.Val1(),GName[:-10],triple.Val2())   
            break
        counter = counter + 1

    number_of_edges_in_traids=snap.GetTriadEdges(G)
    print "Number of edges that participate in at least one triad in {0}: {1}".format(GName[:-10],number_of_edges_in_traids)











def print_ccf_distri(G,GName):

    filename="ccf."+GName[:-10]+".png"
    snap.PlotClustCf(G, GName[:-10], GName[:-10] + " - clustering coefficient")

    print "Clustering coefficient distribution of {0} is in: {1}".format(GName[:-10],filename)










if __name__ == "__main__":

    #Setting Snap Randomized Seed Value to 42 
    Rnd = snap.TRnd(42)
    Rnd.Randomize()

    G,GName = fetch_graph()

    nodes,edges = get_nodes_and_edges(G,GName)
    solve_degree_based_questions(G,GName)
    solve_shortest_path_based_questions(G,GName)
    fraction_of_nodes_in_largest_connected_component(G,GName)
    number_of_bridges(G,GName)
    number_of_articulation_points(G,GName)
    plot_component_size_distribution(G,GName)
    print_average_ccf_and_traid_count(G,GName)
    print_ccf_of_random_node(G,GName)
    print_number_of_traids_participated_by_random_node(G,GName)
    print_ccf_distri(G,GName)

