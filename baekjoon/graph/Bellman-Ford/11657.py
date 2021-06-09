# https://www.acmicpc.net/problem/11657
# Bellman-Ford shortest path
import sys
input = sys.stdin.readline

INF = float('inf')
# INF = int(1e9)

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))


def bellman_ford(edges, start):
    dist = [INF] * (n + 1)
    dist[start] = 0

    for _ in range(n - 1):
        for a, b, cost in edges:
            temp = dist[a] + cost
            if dist[b] > temp:
                dist[b] = temp

    for a, b, cost in edges:
        temp = dist[a] + cost
        if dist[b] > temp:
            return []
    return dist


result = bellman_ford(edges, 1)
if result:
    for b in range(2, n + 1):
        print(result[b]) if result[b] != INF else print(-1)
else:
    print(-1)

'''
input1
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2
output1
4
3

input2
3 4
1 2 4
1 3 3
2 3 -4
3 1 -2
output2
-1

input3
3 2
1 2 4
1 2 3
output3
3
-1

input4: 
3 2
2 3 -2
3 2 -2
output4
-1
-1
'''
