from prims2 import Prims
damauli = Prims(18,'D:\python\Operation_Research\distance_matrix2.csv')
x = damauli.mst()
# print(x)
import matplotlib.pyplot as plt
import networkx as nx
G = nx.DiGraph()
fixed_pos= {}
for i in range(18):
    G.add_node(i+1)
    fixed_pos[i] =(i,i+1)
    
for i in x:
    G.add_edge(i['source'],i['destination'],weight=i['weight'])
# print(G.number_of_edges())
# print(G.number_of_nodes())

pos = nx.spring_layout(G)
plt.figure(figsize=(10,10))
nx.draw(G,pos,with_labels=True,node_size=200)
labels=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

    