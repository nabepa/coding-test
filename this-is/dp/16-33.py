# https://www.acmicpc.net/problem/14501
# 첫 연습때 풀이와 미묘하게 다름!
n = int(input())
t_table = [0]
p_table = [0]

for _ in range(n):
    t, p = map(int, input().split())
    t_table.append(t)
    p_table.append(p)

dp = [0] * (n + 2)

for i in range(n, 0, -1):
    end_day = i + t_table[i]
    if end_day <= n + 1:
        dp[i] = max(dp[i + 1], p_table[i] + dp[end_day])
    else:
        dp[i] = dp[i + 1]

print(dp[1])

'''
input
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
output
45

input
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
output
55

input
10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6
output
20

input
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
output
90
'''
