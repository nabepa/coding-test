# https://www.acmicpc.net/problem/1017
from math import sqrt


def check_primality(n):
    if n == 1:
        return False
    cnt = 0
    i = 1
    while i <= sqrt(n):
        if n % i == 0:
            cnt += 2
            if cnt > 2:
                break
        i += 1
    return True if cnt <= 2 else False


n = int(input())
array = list(map(int, input().split()))
array.sort()

a = array[0]
result = []
# for i in range(1, len(array)):
#     if check_primality(a + array[i]) == True:

# 아직 미완성
