INF = float('inf')

#make cost matrix
vertex, edge = map(int,input().split())

def costmatrix(v,e):
    m = [[None]*v for i in range(v)]
    for i in range(v):
        for j in range(v):
            if i==j :
                m[i][j] = 0
            else:
                m[i][j] = INF
    
    print('give weightage of individual source and destination')
    
    for i in range(e):
        print('s,d,w')
        src,dst,weight = map(int,input().split())
        m[src][dst] = weight
        
    return m

def returnmatrix(v,e,matrix):
    n_a = matrix
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if n_a[i][j] < (n_a[i][k] + n_a[k][j]):
                    n_a[i][j] = n_a[i][j]
                elif n_a[i][j] >= n_a[i][k] + n_a[k][j]:
                    n_a[i][j] = n_a[i][k] + n_a[k][j]
                
    return n_a

a = costmatrix(vertex,edge)
b = returnmatrix(vertex,edge,a)
print(a)
print(b)
        
    

        