# https://www.acmicpc.net/problem/18353
# 전형적인 DP일고리즘인 '가장 긴 증가하는 부분 수열(LIS, Longest Increasing Subsequence)'
# dp[i] = 'array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이'라고 정의
n = int(input())
array = list(map(int, input().split()))
array.reverse()  # 뒤집어서 LIS 문제로

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

'''
input
7
15 11 4 8 5 2 4
output
2
'''
