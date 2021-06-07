# 간선의 값이 모두 1로 동일하므로 BFS 사용하는 것이 사실 더 빨리 구할 수 있음
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (n + 1)

# 시작점
v = 1
q = deque([v])
dist[1] = 0

max_val = 0

while q:
    now = q.popleft()
    cost = dist[now] + 1
    for i in graph[now]:
        if dist[i] == -1:
            dist[i] = cost
            q.append(i)
            max_val = max(max_val, cost)


# 아래와 같이 list의 method 각각 이용하는 것보다, for문 한번에 찾는 것이 좋지만... 엄청난 차이도 아니고 빨리 문제 풀어야할 때는 메소드 사용도 나쁘지 않을 듯!
print(dist.index(max_val), max_val, dist.count(max_val))

'''
input
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2
output
4 2 3
'''
