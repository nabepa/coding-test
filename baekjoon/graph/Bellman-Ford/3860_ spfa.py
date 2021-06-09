# https://www.acmicpc.net/problem/3860
# 3860_bellman.py를 python에서도 시간 초과안하게 SPFA로 도전
# 시간초과로 실패 ...
from collections import defaultdict, deque
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

        graph = defaultdict(list)  # (x, y)를 주소로 가지는 딕셔너리를 이용해 인접 리스트로 그래프 표시
        e = int(input())  # e: 구멍의 개수
        for _ in range(e):
            x1, y1, x2, y2, t = map(int, input().split())
            board[y1][x1] = 2
            graph[(x1, y1)].append(((x2, y2), t))

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
                        graph[(x, y)].append(((nx, ny), 1))

        v = w * h  # 노드의 개수
        dist = [[INF] * w for _ in range(h)]  # 2차원 행렬의 최단 거리 테이블
        dist[0][0] = 0

        q = deque()  # used for SPFA
        q.append((0, 0))
        update_cnt = [[0] * w for _ in range(h)]  # 노드의 갱신 횟수, 음수 순환 탈출용

        is_nc = False  # for checking negative-weight cycle
        while q:
            a = q.popleft()
            x1, y1 = a
            for b, cost in graph[a]:
                x2, y2 = b
                temp = dist[y1][x1] + cost
                if dist[y2][x2] > temp:
                    dist[y2][x2] = temp
                    if b not in q:
                        update_cnt[y2][x2] += 1
                        if update_cnt[y2][x2] >= v:
                            is_nc = True
                            break
                        q.append(b)

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
