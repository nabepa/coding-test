# https://www.acmicpc.net/problem/2580

board = []
spaces = []
for i in range(9):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(9):
        if row[j] == 0:
            spaces.append((i, j))

is_over = False


def check_in_rc(y, x, val):
    for k in range(9):
        if board[y][k] == val or board[k][x] == val:
            return False
    return True


def check_in_box(y, x, val):
    by = y // 3 * 3
    bx = x // 3 * 3
    for i in range(by, by + 3):
        for j in range(bx, bx + 3):
            if board[i][j] == val:
                return False
    return True


def backtracking(idx):
    global is_over
    if is_over:
        return
    elif idx == len(spaces):
        is_over = True
        for row in board:
            print(*row)
        return
    else:
        i, j = spaces[idx]
        candidates = []
        for candidate in range(1, 10):
            if check_in_rc(i, j, candidate) and check_in_box(i, j, candidate):
                candidates.append(candidate)

        for candidate in candidates:
            board[i][j] = candidate
            backtracking(idx + 1)
            board[i][j] = 0


backtracking(0)

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
