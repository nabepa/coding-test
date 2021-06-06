# https://www.acmicpc.net/problem/14888
# DFS, BFS로도 풀 수 있지만 조금 귀찮음
INF = 1e9
max_val = -INF
min_val = INF

n = int(input())
array = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())


def dfs(num, cnt):
    global max_val, min_val
    global add, sub, mul, div
    if cnt == n:
        max_val = max(max_val, num)
        min_val = min(min_val, num)
    else:
        if add > 0:
            add -= 1
            dfs(num + array[cnt], cnt + 1)
            add += 1
        if sub > 0:
            sub -= 1
            dfs(num - array[cnt], cnt + 1)
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(num * array[cnt], cnt + 1)
            mul += 1
        if div > 0:
            div -= 1
            dfs(int(num / array[cnt]), cnt + 1)  # 나누기 연산에 // 쓰면 안됨
            div += 1


dfs(array[0], 1)
print(max_val)
print(min_val)

'''
input
2
5 6
0 0 1 0
output
30
30

input
3
3 4 5
1 0 1 0
output
35
17

input
6
1 2 3 4 5 6
2 1 1 1
output
54
-24
'''
