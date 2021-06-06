# https://www.acmicpc.net/problem/3190
from collections import deque

EMPTY = 0
APPLE = 1
SNAKE = 2

n = int(input())  # n X n board
k = int(input())  # number of apples

board = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = APPLE

l = int(input())  # number of changing direction
commands = []
for _ in range(l):
    t, command = input().split()
    commands.append((int(t), command))

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

hy, hx = 1, 1
board[hy][hx] = SNAKE
direction = 0
t = 0  # time
command_idx = 0
snake = deque([(hy, hx)])  # snake, index 0 is coordinate of head
while True:
    t += 1

    ny = hy + dy[direction]
    nx = hx + dx[direction]
    if 1 <= ny <= n and 1 <= nx <= n and board[ny][nx] != SNAKE:
        if board[ny][nx] == EMPTY:
            ty, tx = snake.pop()
            board[ty][tx] = EMPTY
        board[ny][nx] = SNAKE
        hy, hx = ny, nx
        snake.appendleft((hy, hx))
    else:
        break

    if command_idx < l and t == commands[command_idx][0]:
        if commands[command_idx][1] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        command_idx += 1

print(t)

'''
input
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
output
9

input
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
output
21

input
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
output
13
'''
