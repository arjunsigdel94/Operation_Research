import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import networkx as nx

Inf = float('inf')


class Prims:
    def __init__(self,vertex,file_location):
        self.vertex = vertex 
        self.file_location = file_location
    
    def distance_matrix(self):
        costmatrix = [[0 for i in range(self.vertex)]for j in range(self.vertex)]
        csvfile = pd.read_csv(self.file_location,header=None)
        
        for i in range(self.vertex):
            for j in range(self.vertex):
               costmatrix[i][j] = csvfile.iloc[i,j]
        
        adjacency_matrix = np.array(costmatrix)
    
        return adjacency_matrix
    
    def mst(self):
        stored_vertex = [False for i in range(self.vertex)]
        stored_vertex[0] = [True]
        final_tree = []
        self.costmatrix = self.distance_matrix()

        no_edge = 0
        while (no_edge < self.vertex-1) :
            x = 0
            y = 0
            min = Inf
            for i in range(self.vertex):
                if stored_vertex[i]:
                    #find adjacent node
                    for j in range(self.vertex):
                        if ((not stored_vertex[j]) and self.costmatrix[i][j]):
                            #above statement find new node with edge
                            if min > self.costmatrix[i][j] :
                                min = self.costmatrix[i][j]
                                x = i
                                y = j
                        
    
            final_tree.append({'source' : (x+1),'destination' : (y+1), 'weight' : self.costmatrix[x][y]})               
            stored_vertex[y] = True
            no_edge += 1
        
        return final_tree
    
    def draw_tree(self):
        G = nx.DiGraph()
        fixed_pos= {}
        self.final_tree=self.mst()
        for i in range(18):
            G.add_node(i+1)
            fixed_pos[i] =(i,i+1)
    
        for i in self.final_tree:
            G.add_edge(i['source'],i['destination'],weight=i['weight'])
            # print(G.number_of_edges())
            # print(G.number_of_nodes())

        pos = nx.spring_layout(G)
        plt.figure(figsize=(10,10))
        nx.draw(G,pos,with_labels=True,node_size=200)
        labels=nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
        plt.show()
    
    
    
damauli = Prims(18,'D:\python\Operation_Research\distance_matrix2.csv')
x = damauli.draw_tree()

        
    
        
        