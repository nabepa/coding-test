# https://www.acmicpc.net/problem/2580
import sys

N = 9
TOTAL = sum(range(1, 10)) * 9


def check_in_box(board, y, x, val):
    ry = y % 3
    rx = x % 3
    for i in range(y - ry, y + (3 - ry)):
        for j in range(x - rx, x + (3 - rx)):
            if board[y][x] == val:
                return False
    return True


def backtracking(board, empty, total, cnt):
    if not empty:
        if cnt == total:
            for row in board:
                for elem in row:
                    print(elem, end=' ')
                print()
            sys.exit(0)
    else:
        i, j = empty.pop()
        for val in range(1, N + 1):
            is_ok = True
            for k in range(N):
                if board[i][k] == val or board[k][j] == val:
                    is_ok = False
                    break
            if is_ok:
                is_ok = check_in_box(board, i, j, val)
            if is_ok:
                board[i][j] = val
                backtracking(board, list(empty), total, cnt + 1)
                board[i][j] = 0


def solution():
    empty = []
    board = []
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        for j in range(N):
            if board[i][j] == 0:
                empty.append((i, j))

    backtracking(board, empty, len(empty), 0)


if __name__ == '__main__':
    solution()

'''
input
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0
output
1 3 5 4 6 9 2 7 8
7 8 2 1 3 5 6 4 9
4 6 9 2 7 8 1 3 5
3 2 1 5 4 6 8 9 7
8 7 4 9 1 3 5 2 6
5 9 6 8 2 7 4 1 3
9 1 7 6 5 2 3 8 4
6 4 3 7 8 1 9 5 2
2 5 8 3 9 4 7 6 1
'''
