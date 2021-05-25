INF  = float('inf')
# def printmatrix(m):
#     r,c = len(m),len(m[0])
#     for i in range(r):
#         for j in range(c):
#             print(m[i][j],end=" ")
#         print()
        
# v,e = map(int,input().split())
# m = [[None]*v for i in range(v)]
# for i in range(v):
#     for j in range(v):
#         #src = dst
#         if i == j:
#             m[i][j] = 0
#         # edge doesn't exist
#         else:
#             m[i][j] = INF
            
# #take input values
# for i in range(e):
#     src,dst,wt = map(int,input().split())
#     m[src][dst] = wt
    
class ShortestPath:
    def __init__(self,vertex,edge):
        self.vertex = vertex
        self.edge = edge
    
    def inputmatrix(self):
        m = [[None]*v for i in range(v)]
        for i in range(self.vertex):
            for j in range(self.vertex):
                #when source = distance
                if i == j:
                    m[i][j] = 0
                
                else:
                    m[i][j] = INF
        
        for i in range(self.edge):
            print('s,d,w')
            src,dst,weight = map(int,input().split())
            m[src,dst] = weight
        
        return inputmatrix
    
    def calculate_shortest_path(self):
        m = self.inputmatrix
        for k in range(self.vertex):
            for i in range(self.vertex):
                 for j in range(self.vertex):
                     if m[i][j] < (m[i][k] + m[k][j]):
                         m[i][j] = m[i][j]
                     else:
                         m[i][j] = m[i][k] + m[k][j]
        
        return m
    
x = ShortestPath(5,7)
x.calculate_shortest_path      
        
                
            
    
    
                    
        
    

