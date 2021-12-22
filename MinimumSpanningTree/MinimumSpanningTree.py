### MINIMUM SPANNING TREE

import networkx as nx
import random
import matplotlib.pyplot as plt

GraphMatrix = []
NodesNumber = 5
def empty_graph(nodes, graphlist):
    graphlist =[[0 for _j in range(nodes)] for _i in range(nodes)]
    return graphlist

def randomise_weights(nodes, graphlist):
    for node1 in range(nodes):
        for node2 in range(nodes):
            weight = random.randint(0, 3)
            if node1 != node2:
                graphlist[node1][node2] = weight
                graphlist[node2][node1] = weight
    for l in range(len(graphlist)):
        graphlist[l] = tuple(graphlist[l])
    return graphlist

def create_graph(graph, graphtuple, nodes):
    for node1 in range(nodes):
        for node2 in range(node1 + 1, nodes):
            graph.add_edge('N' + str(node1), 'N' + str(node2), weight = graphtuple[node1][node2])
#print(GraphMatrix)
GraphMatrix = empty_graph(NodesNumber, GraphMatrix)
GraphMatrix = randomise_weights(NodesNumber, GraphMatrix)
G = nx.Graph()
create_graph(G, GraphMatrix, NodesNumber)
nx.draw_networkx(G)
#print(nx.to_dict_of_dicts(G))
#nx.add_edgedraw_networkx_edge_labels(G, pos=nx.to_dict_of_dicts(G)) 
plt.show()

pos=nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
plt.show()

