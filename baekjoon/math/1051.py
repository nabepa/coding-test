n, m = map(int, input().split())

board = []
for _ in range(n):
    row = list(map(int, input()))
    board.append(row)

max_len = min(n, m)

b_over = False
while max_len > 1:
    for i in range(n - max_len + 1):
        if b_over:
            break
        for j in range(m - max_len + 1):
            lu = board[i][j]  # left up
            idx_r = j + max_len - 1
            idx_d = i + max_len - 1
            if idx_r < m and idx_d < n and lu == board[idx_d][j] and lu == board[i][idx_r] and lu == board[idx_d][idx_r]:
                b_over = True
                break

    if b_over:
        break
    max_len -= 1

print(max_len ** 2)

'''
input
3 5
42101
22100
22101
output
9
'''
