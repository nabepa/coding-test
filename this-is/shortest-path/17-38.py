# Floyd-Warshall
# 참고로 모든 노드의 정확한 진입차수를 알 수 없으므로, 위상정렬로는 풀 수 없을 것임!
INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF and graph[j][i] == INF:
            break
        if j == n:
            result += 1

print(result)

'''
input
6 6
1 5
3 4
4 2
4 6
5 2
5 4
'''
