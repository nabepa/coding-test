# Search shortest paths (single->all)
# useful for graphs in which some of the edge weights are negative

# INF = int(1e9)
INF = float('inf')

v, e = map(int, input().split())  # len of vertex, edge
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())  # a->b' cost
    edges.append((a, b, cost))


def bellman_ford(edges, start):
    dist = [INF] * (v + 1)
    dist[start] = 0

    # Relax edges v-1 times
    for _ in range(v - 1):
        for a, b, cost in edges:
            temp = dist[a] + cost
            if dist[b] > temp:
                dist[b] = temp

    # Check for negative cycle
    for a, b, cost in edges:
        temp = dist[a] + cost
        if dist[b] > temp:
            return []
    return dist


result = bellman_ford(edges, 1)
if result:
    for b in range(2, v + 1):
        print(result[b]) if result[b] != INF else print(-1)
else:
    print(-1)

'''
input
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2
output
4
3
'''
