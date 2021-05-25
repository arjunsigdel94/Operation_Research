import numpy as np
from numpy.core.numeric import Inf
import pandas as pd 

INF = float('inf')
# def costmatrix(v,e):
#     m = [[None]*v for i in range(v)]
#     for i in range(v):
#         for j in range(v):
#             if i==j :
#                 m[i][j] = 0
#             else:
#                 m[i][j] = INF
    
#     print('give weightage of individual source and destination')
    
#     for i in range(e):
#         print('s,d,w')
#         src,dst,weight = map(int,input().split())
#         m[src][dst] = weight
        
#     return m


v = int(input('enter number of vertex: '))
# e = int(input('number of edges: '))

costmatrix = [[0 for i in range(v)]for j in range(v)]
csvfile = pd.read_csv('D:\python\Operation_Research\distance_matrix2.csv',header=None)

for i in range(v):
    for j in range(v):
        costmatrix[i][j] = csvfile.iloc[i,j]
        
adjacency_matrix = np.array(costmatrix)




print(adjacency_matrix)

# finding shortest path
stored_vertex = [False for i in range(v)]
stored_vertex[0] = [True]
final_tree = []

no_edge = 0
while (no_edge < v-1) :
    x = 0
    y = 0
    min = Inf
    for i in range(v):
        if stored_vertex[i]:
        #find adjacent node
            for j in range(v):
                if ((not stored_vertex[j]) and costmatrix[i][j]):
                #above statement find new node with edge
                    if min > costmatrix[i][j] :
                        min = costmatrix[i][j]
                        x = i
                        y = j
                        
    
    final_tree.append({'source' : str(x+1),'destination' : str(y+1), 'weight' : costmatrix[x][y]})               
    stored_vertex[y] = True
    no_edge += 1

for i in final_tree:
    print(i)
                    
                        
       
    
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

        no_edge = 0
        while (no_edge < self.vertex-1) :
            x = 0
            y = 0
            min = Inf
            for i in range(self.vertex):
                if stored_vertex[i]:
                    #find adjacent node
                    for j in range(self.vertex):
                        if ((not stored_vertex[j]) and costmatrix[i][j]):
                            #above statement find new node with edge
                            if min > costmatrix[i][j] :
                                min = costmatrix[i][j]
                                x = i
                                y = j
                        
    
            final_tree.append({'source' : str(x+1),'destination' : str(y+1), 'weight' : costmatrix[x][y]})               
            stored_vertex[y] = True
            no_edge += 1
        
        return final_tree
        
        
        
        

