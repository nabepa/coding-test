# https://www.acmicpc.net/problem/2110
# Parametric Search
import sys
input = sys.stdin.readline

n, c = map(int, input().split())

houses = []
for _ in range(n):
    houses.append(int(input()))

houses.sort()

gap_min = 1
gap_max = houses[-1] - houses[0]
result = 1

while gap_min <= gap_max:
    x = (gap_min + gap_max) // 2

    # gap이 x일 때 몇개 설치할 수 있는지 확인
    prev = houses[0]
    cnt = 1
    for i in range(1, n):
        if houses[i] >= prev + x:
            prev = houses[i]
            cnt += 1

    if cnt >= c:
        gap_min = x + 1
        result = x
    else:
        gap_max = x - 1

print(result)

'''
input
5 3
1
2
8
4
9
output
3
'''
