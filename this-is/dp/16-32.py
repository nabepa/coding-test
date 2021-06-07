# https://www.acmicpc.net/problem/1932
n = int(input())

figure = []
for _ in range(n):
    figure.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            figure[i][j] += figure[i - 1][j]
        elif j == i:
            figure[i][j] += figure[i - 1][j - 1]
        else:
            figure[i][j] += max(figure[i - 1][j], figure[i - 1][j - 1])

result = max(figure[n - 1])
print(result)

'''
input
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
output
30
'''
