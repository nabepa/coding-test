# Search shortest paths (all->all)
INF = int(1e9)

v, e = map(int, input().split())  # len of vertex and edge

# Initialize a adjacency matrix
graph = [[INF] * (v + 1) for _ in range(v + 1)]
for a in range(1, v + 1):
    graph[a][a] = 0

# Get graph' info
for _ in range(e):
    a, b, cost = map(int, input().split())  # a->b' cost
    graph[a][b] = cost

# Floyd-Warshall
for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# Print result
for a in range(1, v + 1):
    for b in range(1, v + 1):
        if graph[a][b] == INF:  # No path
            print(-1, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

'''
input
4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
output
0 4 8 6 
3 0 7 9 
5 9 0 4 
7 11 2 0 
'''
