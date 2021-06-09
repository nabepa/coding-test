# https://www.acmicpc.net/problem/1747
import math
from bisect import bisect_left


def find_primes_until(n):
    array = [True for i in range(n + 1)]

    # Eratosthenes' sieve
    for i in range(2, int(math.sqrt(n)) + 1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    result = []
    for i in range(2, n + 1):
        if array[i]:
            result.append(i)

    return result


def check_primality(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# def check_palindrome(n):
#     origin = n
#     reversed = 0

#     while origin > 0:
#         reversed = reversed * 10 + origin % 10
#         origin //= 10

#     return reversed == n

# 다른 언어에서는 팰린드린 수인지 위에 코멘트 아웃한 방법을 쓰겠지만, 파이썬은 아래와 같은 방법으로 쓰는게 가장 간단
def check_palindrome(n):
    return str(n) == str(n)[::-1]


primes = find_primes_until(1000000)

n = int(input())
idx = bisect_left(primes, n)

result = -1
while idx < len(primes):
    prime = primes[idx]

    if check_palindrome(prime):
        result = prime
        break

    idx += 1

# 100만 까지 소수를 구했지만... 예를들어 n=100만이면, 그 이후의 수중 소수이면서 팰린드린 수인 값을 찾아야함
if result == -1:
    i = 1000000
    while True:
        i += 1
        if not check_primality(i):
            continue
        if check_palindrome(i):
            result = i
            break

print(result)

'''
input
31
output
101
'''
