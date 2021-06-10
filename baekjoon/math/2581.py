# https://www.acmicpc.net/problem/2581
# 소수
import math
from bisect import bisect_left


def find_primes_until(n):
    array = [True for i in range(n + 1)]

    # Eratosthenes' sieve
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:  # i가 남은 수인 경우
            # i를 제외한 i의 모든 배수 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    result = []
    for i in range(2, n + 1):
        if array[i]:
            result.append(i)

    return result


# m 이상 n 이하 소수 찾기
m = int(input())
n = int(input())

primes = find_primes_until(n)
idx = bisect_left(primes, m)

if idx >= len(primes):
    print(-1)
else:
    print(sum(primes[idx:]))
    print(primes[idx])

'''
input
60
100
output
620
61

input
64
65
output
-1
'''
