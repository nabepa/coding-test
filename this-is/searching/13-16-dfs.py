# https://www.acmicpc.net/problem/14502
# dfs 좋은 연습이자 교과서 풀이지만, bfs 쪽 알고리즘이 빠름
from copy import deepcopy

SPACE = 0
WALL = 1
VIRUS = 2

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, input().split())

board = []
virus = []
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(m):
        if row[j] == VIRUS:
            virus.append((i, j))

max_val = 0


# spread virus by dfs
def simulate(board, vy, vx):
    for i in range(4):
        ny = vy + dy[i]
        nx = vx + dx[i]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == SPACE:
            board[ny][nx] = VIRUS
            simulate(board, ny, nx)


# dfs
def calc_max_safe_zone(cnt_wall):
    global max_val

    if cnt_wall == 3:
        n_board = deepcopy(board)
        for vy, vx in virus:
            simulate(n_board, vy, vx)

        cnt_safe_zone = 0
        for i in range(n):
            for j in range(m):
                if n_board[i][j] == SPACE:
                    cnt_safe_zone += 1

        max_val = max(max_val, cnt_safe_zone)

        return

    for i in range(n):
        for j in range(m):
            if board[i][j] == SPACE:
                board[i][j] = WALL
                calc_max_safe_zone(cnt_wall + 1)
                board[i][j] = SPACE


calc_max_safe_zone(0)
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
