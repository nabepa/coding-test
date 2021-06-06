# https://www.acmicpc.net/problem/18352
# BFS
from collections import deque
import sys

input = sys.stdin.readline

# n: 도시의 개수, m: 도로의 개수, k: 거리 정보, x: 출발 도시
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n + 1)

result = []
q = deque([x])
dist[x] = 0

while q:
    now = q.popleft()
    for v in graph[now]:
        if dist[v] == -1:
            dist[v] = dist[now] + 1
            q.append(v)

            if dist[v] == k:
                result.append(v)

if len(result) == 0:
    print(-1)
else:
    result.sort()
    for v in result:
        print(v)
