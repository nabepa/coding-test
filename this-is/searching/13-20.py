# https://www.acmicpc.net/problem/18428
# BFS/DFS 비스무리한 문제
from itertools import combinations
from copy import deepcopy

n = int(input())

teachers = []
space = []
board = []
for i in range(n):
    row = input().split()
    board.append(row)
    for j in range(n):
        if row[j] == 'T':
            teachers.append((i, j))
        elif row[j] == 'X':
            space.append((i, j))

candidates = list(combinations(space, 3))


def watch(board):
    for i, j in teachers:
        up = i - 1
        while up >= 0:
            if board[up][j] == 'S':
                return False
            elif board[up][j] == 'O':
                break
            up -= 1

        down = i + 1
        while down < n:
            if board[down][j] == 'S':
                return False
            elif board[down][j] == 'O':
                break
            down += 1

        left = j - 1
        while left >= 0:
            if board[i][left] == 'S':
                return False
            elif board[i][left] == 'O':
                break
            left -= 1

        right = j + 1
        while right < n:
            if board[i][right] == 'S':
                return False
            elif board[i][right] == 'O':
                break
            right += 1

    return True


b_possible = False
for candi in candidates:
    n_board = deepcopy(board)
    for i, j in candi:
        n_board[i][j] = 'O'

    if watch(n_board) == True:
        b_possible = True
        break

print('YES') if b_possible else print('NO')

'''
input
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X
output
YES

input
4
S S S T
X X X X
X X X X
T T T X
output
NO
'''
