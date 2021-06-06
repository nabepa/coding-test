# https://www.acmicpc.net/problem/14502
# bfs
from collections import deque
from itertools import combinations
from copy import deepcopy

SPACE = 0
WALL = 1
VIRUS = 2

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, input().split())

board = []
space, wall, virus = [], [], []
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(m):
        if row[j] == SPACE:
            space.append((i, j))
        elif row[j] == WALL:
            wall.append((i, j))
        else:
            virus.append((i, j))

max_val = 0
candidates = (combinations(space, 3))
for w1, w2, w3 in candidates:
    n_board = deepcopy(board)
    n_board[w1[0]][w1[1]] = WALL
    n_board[w2[0]][w2[1]] = WALL
    n_board[w3[0]][w3[1]] = WALL

    q = deque(virus)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and n_board[ny][nx] == SPACE:
                n_board[ny][nx] = VIRUS
                q.append((ny, nx))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if n_board[i][j] == 0:
                cnt += 1
    max_val = max(max_val, cnt)

print(max_val)
'''
input
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
output
27

input
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
output
9

input
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
output
3
'''
