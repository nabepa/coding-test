# Search shortest paths (single->all)
import heapq

INF = int(1e9)

v, e = map(int, input().split())  # len of vertex, edge
start = int(input())  # start node
graph = [[] for _ in range(v + 1)]  # adjacency list
distance = [INF] * (v + 1)  # shortest table

# edges
for _ in range(e):
    a, b, cost = map(int, input().split())  # a->b' cost
    graph[a].append((b, cost))


def dijkstra(start):
    # add start node into priority queue
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # until the queue is empty
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # pass visited node
            continue
        for i in graph[now]:  # check nodes connected with 'now'
            cost = dist + i[1]
            # if it is shorter to go through 'now',
            if cost < distance[i[0]]:
                distance[i[0]] = cost  # update
                heapq.heappush(q, (cost, i[0]))  # and add into the queue


dijkstra(start)

for i in range(1, v + 1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])

'''
input
6 11
1 
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
output
0
2
3
1
'''
