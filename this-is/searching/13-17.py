from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, k = map(int, input().split())  # n X n 시험관, k 종류의 바이러스

board = []
info = []
for i in range(n):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(n):
        if row[j] != 0:
            info.append((row[j], 0, i, j))  # 바이러스 번호, 시간, i행, j열


s, tar_i, tar_j = map(int, input().split())  # s초 후, i행 j열 확인

info.sort()
q = deque(info)
while q:
    virus_type, t, y, x = q.popleft()
    if t == s:
        break

    for idx in range(4):
        ny = y + dy[idx]
        nx = x + dx[idx]
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
            board[ny][nx] = virus_type
            q.append((virus_type, t + 1, ny, nx))

print(board[tar_i - 1][tar_j - 1])

'''
input
3 3
1 0 2
0 0 0
3 0 0
2 3 2
output
3

input
3 3
1 0 2
0 0 0
3 0 0
1 2 2
output
0
'''
