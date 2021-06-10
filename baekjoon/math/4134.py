# https://www.acmicpc.net/problem/4134
# 다음 소수
import math


def check_primality(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    n = int(input())

    if n <= 2:
        print(2)
        continue

    if n % 2 == 0:
        n += 1

    while True:
        if check_primality(n) == True:
            print(n)
            break
        n += 2

'''
# 요풀이는 인덱스 오류 남 왜일까~~~?
import math


def find_primes_until(n):
    array = [True for i in range(n + 1)]

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


def find_nth_prime(n):
    if n < 6:
        primes = [2, 3, 5, 7, 11]
        return primes[n - 1]
    else:
        limit = math.ceil(n * math.log(n) + n * math.log(math.log(n)))
        primes = find_primes_until(limit)
        return primes[n - 1]


for _ in range(int(input())):
    n = int(input())
    primes = find_primes_until(n)
    if primes[-1] == n:
        print(primes[-1])
    else:
        print(find_nth_prime(len(primes) + 1))
'''
'''
input
3
6
20
100
output
7
23
101
'''
