# Dijkstra
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(int(input())):
    n = int(input())

    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    dist = [[INF] * n for _ in range(n)]

    # 시작점
    y, x = 0, 0
    q = [(board[y][x], y, x)]
    dist[y][x] = board[y][x]

    while q:
        d, y, x = heapq.heappop(q)

        if dist[y][x] < d:
            continue
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                cost = d + board[ny][nx]
                if cost < dist[ny][nx]:
                    dist[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))

    print(dist[n - 1][n - 1])

'''
input
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
output
20
19
36
'''
