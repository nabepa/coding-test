from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)

for _ in range(int(input())):
    n = int(input())
    last_year = list(map(int, input().split()))

    # 위상 정렬할 때는 인접 리스트로 표현한 그래프가 편하지만, 순서 바꾸는 것은 행렬로 표현한 그래프가 편함
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0

    indegree = [0] * (n + 1)
    for i in range(n):
        winner = last_year[i]
        indegree[winner] = i
        for j in range(i + 1, n):
            looser = last_year[j]
            graph[winner][looser] = 1  # 순위 높은 팀->낮은 팀일 때 경로 1이라고 지정!

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b] == INF:  # a < b였다면
            graph[a][b] = 1
            graph[b][a] = INF
            indegree[a] -= 1
            indegree[b] += 1
        else:
            graph[a][b] = INF
            graph[b][a] = 1
            indegree[a] += 1
            indegree[b] -= 1

    # 위상 정렬을 위해 인접 리스트로 표현한 그래프를 새로 생성
    list_graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i][j] == 1:
                list_graph[i].append(j)
            else:
                list_graph[j].append(i)

    this_year = []
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            this_year.append(i)

    # 위상 정렬시 큐의 길이가 의미하는 바
    # 1. 길이 = 0(도중에 큐가 빈다): 데이터에 일관성이 없어, 새로 진입차수가 0이 된 요소가 없다는 것...즉 사이클 발생을 의미
    # 2. 길이 > 1: 동시에 진입차수가 0이 된 요소가 있다는 것, 서로간의 순서를 정확히 알 수 없는 애들...즉 복수개의 순서가 나올 수 있다
    b_cycle = False
    b_oneway = True

    for i in range(n):
        if len(q) == 0:
            b_cycle = True
            break
        elif len(q) > 1:
            b_oneway = False
            break

        v = q.popleft()
        for i in list_graph[v]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                this_year.append(i)

    if b_cycle:
        print('IMPOSSIBLE')
    elif not b_oneway:
        print('?')
    else:
        for i in this_year:
            print(i, end=' ')
        print()

'''
input
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3
output
5 3 2 4 1
2 3 1
IMPOSSIBLE
'''
