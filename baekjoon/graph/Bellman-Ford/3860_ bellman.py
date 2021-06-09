# https://www.acmicpc.net/problem/3860
# 번역에는 명확하게 표시 안됐지만 원문의 출력 조건을 보면,도착지와 사이클이 이어졌는지는 확인안해도 된다.
# "if it is possible for Scared John to travel back in time indefinitely, output Never."
# "Otherwise ~ and Impossible if not".
# 각 노드는 (x, y)로 표시되고, 노드의 총 개수는 w*h
# 춟발지에서의 최단거리는 2차원의 최단거리 테이블을 사용하면 됨
# 구멍 시작 -> 구멍 끝 간선 & (x,y)->상하좌우의 간선들에 대해 Bellman-Ford
import sys
input = sys.stdin.readline

INF = float('inf')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def solution():
    while True:
        w, h = map(int, input().split())  # w X h
        if w == 0 and h == 0:
            break

        board = [[0] * w for _ in range(h)]  # 잔디, 묘비, 구멍의 위치 표시

        g = int(input())  # g: 묘비의 개수
        for _ in range(g):
            x, y = map(int, input().split())
            board[y][x] = 1

        edges = []  # 모든 간선
        e = int(input())  # e: 구멍의 개수
        for _ in range(e):
            x1, y1, x2, y2, t = map(int, input().split())
            board[y1][x1] = 2
            edges.append(((x1, y1), (x2, y2), t))

        # 잔디에서 노드 뻗기
        for y in range(h):
            for x in range(w):
                # 묘지는 물론, 골에서도 노드 뻗지 않음(상근이는 골에 도착하면 빤스런)
                if board[y][x] != 0 or (y == h - 1 and x == w - 1):
                    continue
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < h and 0 <= nx < w and board[ny][nx] != 1:
                        edges.append(((x, y), (nx, ny), 1))

        v = w * h  # 노드의 개수
        dist = [[INF] * w for _ in range(h)]  # 2차원 행렬의 최단 거리 테이블
        dist[0][0] = 0

        # v-1 times relax
        for _ in range(v - 1):
            for a, b, cost in edges:
                x1, y1 = a
                x2, y2 = b
                temp = dist[y1][x1] + cost
                if dist[y2][x2] > temp:
                    dist[y2][x2] = temp

        is_nc = False  # for checking negative-weight cycle
        for a, b, cost in edges:
            x1, y1 = a
            x2, y2 = b
            temp = dist[y1][x1] + cost
            if dist[y2][x2] > temp:
                is_nc = True
                break

        # 순서 주의!골 도달 못해도, 음수 순환에 도달하면 Never 출력
        if is_nc:
            print('Never')
        elif dist[h - 1][w - 1] == INF:
            print('Impossible')
        else:
            print(dist[h - 1][w - 1])


if __name__ == '__main__':
    solution()

'''
input
3 3
2
2 1
1 2
0
4 3
2
2 1
3 1
1
3 0 2 2 0
4 2
0
1
2 0 1 0 -3
0 0
output
Impossible
4
Never

input
5 5
11
0 1
0 2
0 3
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
1
0 4 1 0 -11
0 0
output
8

input
5 5
11
0 1
0 2
0 3
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
1
0 4 1 0 -12
output
Never

input: 목적지 도달 못하지만, 음수순환 도달하는 경우
4 3
2
2 2
3 1
1
1 1 0 0 -3
0 0
output
Never
'''
