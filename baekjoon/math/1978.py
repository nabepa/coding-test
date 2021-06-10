# https://www.acmicpc.net/problem/1978
# 소수 찾기
import math


def check_primality(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


n = input()
array = list(map(int, input().split()))

cnt = 0
for a in array:
    if check_primality(a):
        cnt += 1

print(cnt)

'''
input
4
1 3 5 7
output
3
'''
