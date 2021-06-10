# https://www.acmicpc.net/problem/10942
#  팰린드롬 & DP
import sys
input = sys.stdin.readline

n = int(input())
array = input().split()
array = ['0'] + array

# dp[a][b] = array[a][b]가 팰린드롬 수인지
dp = [[False] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = True

# 길이가 작은 수열부터 팰린드롬 수인지 확인
# 그러면 양끝 확인 + 가운데 부분(dp에 결과 불러오기만 하면 됨) 확인은로 펠린드롬 수인지 확인 가능
for length in range(2, n + 1):
    for i in range(1, n - length + 2):
        left_idx = i
        right_idx = i + length - 1
        if array[left_idx] != array[right_idx]:
            continue

        if length == 2:
            dp[left_idx][right_idx] = True
            continue

        if dp[left_idx + 1][right_idx - 1] == True:
            dp[left_idx][right_idx] = True

for _ in range(int(input())):
    a, b = map(int, input().split())
    if dp[a][b] == True:
        print(1)
    else:
        print(0)

'''
input
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
output
1
0
1
1

input
7
1 2 2 1 3 1 3
4
1 4
4 6
5 7
4 7
output
1
1
1
0
'''
