# https://www.acmicpc.net/problem/1865
import sys
input = sys.stdin.readline

# 최단경로를 직접 구할 필요없이, 전체 경로 중에 음수 순환이 존재하는지만 빠르게 파악하고 싶은 경우
# INF = float('inf')를 사용하면 도달하지 못하는 음수 순환 감지 못해서, 모든 노드를 시작점으로 해봐야함
# 하지만 INF를 큰 정수 값으로 하면, 한 노드 확인만 하면 도달하지 못하는 음수 순환도 감지 가능
INF = int(1e9)


def check_timetravel(edges, n):
    # Bellman-Ford
    dist = [INF] * (n + 1)
    dist[1] = 0
    for _ in range(n - 1):
        for a, b, cost in edges:
            temp = dist[a] + cost
            if dist[b] > temp:
                dist[b] = temp
    for a, b, cost in edges:
        temp = dist[a] + cost
        if dist[b] > temp:
            return True
    return False


def solution():
    for _ in range(int(input())):
        n, m, w = map(int, input().split())  # n: vertex, m: path, w: wormhole

        # 중복되는 경로 중 최소값만 남길때 인접행렬이 간편
        graph = [[INF] * (n + 1) for _ in range(n + 1)]
        # 나중에 경로가 INF 아닌 애들만 edge 넣어주는데, 자신에서 자신으로 가는 경우도 넣어주기 싫으니까 밑에 코드도 쓰지말자
        # for i in range(1, n + 1):
        # graph[i][i] = 0

        for _ in range(m):
            a, b, cost = map(int, input().split())  # a->b' cost
            graph[a][b] = min(graph[a][b], cost)
            graph[b][a] = min(graph[b][a], cost)
        for _ in range(w):
            a, b, cost = map(int, input().split())  # a->b' cost
            graph[a][b] = min(graph[a][b], -cost)

        # 존재하는 간선만 모으기
        edges = []
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] != INF:
                    edges.append((i, j, graph[i][j]))

        # 시간 여행 가능한지 확인
        print('YES') if check_timetravel(edges, n) else print('NO')


if __name__ == '__main__':
    solution()
