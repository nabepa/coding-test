# https://www.acmicpc.net/problem/1977
# 완전제곱수
import math

m = int(input())
n = int(input())

# i * i <= m인 i가 구해짐
i = int(math.sqrt(m))

# i * i == m이면 이게 m 이상 n 이하의 가장 작은 완전 제곱수 '후보'
# 후보인 이유는 아래에서
min_val = i * i

# i * i != m이라는 것은 m은 제곱수가 아닌 거고, 이때 최소 제곱수 '후보'는 (i + 1)**2
if min_val != m:
    i += 1
    min_val = i * i

if min_val > n:  # 만약 위에서 구한 최소 제곱수가 n보다 크다면 m 이상 n 이하에는 제곱수가 없다는 것
    print(-1)
else:
    sum_val = min_val
    while True:
        i += 1
        now = i * i
        if now > n:
            break
        sum_val += now

    print(sum_val)
    print(min_val)

'''
input
60
100
output
245
64

input
75
80
output
-1
'''
