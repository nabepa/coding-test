# https://www.acmicpc.net/problem/1219
# https://blog.naver.com/shcoqkrtk/222322465121
# 실수 1. 출발지에서 벌 수 있는 금액을 무시함
# 실수 2. 음수 순환이 출발지 뿐만 아니라 도착지에도 연결되어 있어야 함
# 실수 3. 음수 순환이 출발지와 도착지 모두에 연결되어 있어도 Relax를 무척 많이 해야 갱신되는 경우가 있음
from collections import deque

INF = float('inf')

n, start, goal, m = map(int, input().split())

graph = [[] for _ in range(n)]  # BFS
edges = []  # Bellman-Ford
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((a, b, cost))
    graph[a].append(b)

incomes = list(map(int, input().split()))


# BFS를 이용한 음수 순환에서 도착지까지의 연결 여부 확인
def check_connection_with_goal(a):
    visited = [False] * n
    visited[a] = True
    q = deque([a])
    while q:
        v = q.popleft()
        for i in graph[v]:
            if i == goal:
                return True
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return False


def solution():
    # V-1 times relax
    dist = [INF] * n
    dist[start] = -incomes[start]
    for _ in range(n - 1):
        for a, b, cost in edges:
            temp = dist[a] + cost - incomes[b]
            if dist[b] > temp:
                dist[b] = temp

    # V-th relax
    is_rich = False
    for a, b, cost in edges:
        temp = dist[a] + cost - incomes[b]
        if dist[b] > temp:
            if check_connection_with_goal(b):  # 음수 순환에서 도착까지 연결된 경우
                is_rich = True
                break

    if dist[goal] == INF:
        print('gg')
    elif is_rich:
        print('Gee')
    else:
        print(-dist[goal])


if __name__ == '__main__':
    solution()

'''
input1
5 0 4 7
0 1 13
1 2 17
2 4 20
0 3 22
1 3 4747
2 0 10
3 4 10
0 0 0 0 0
output1
-32

input: 출발지에서 도달할 수 있는 음수순환이 도착지에는 연결안된 경우
4 0 3 4
0 1 0
1 2 0
2 1 0
0 3 10
10 10 10 10
output
10

check other 5 test sample in the link
'''
