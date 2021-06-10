# https://www.acmicpc.net/problem/11653
# 소인수분해
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


n = int(input())

primes = find_primes_until(n)

result = []
divided = n
idx = 0

while divided > 1:
    prime = primes[idx]
    if divided % prime == 0:
        result.append(prime)
        divided //= prime
    else:
        idx += 1

for r in result:
    print(r)

'''
input
72
output
2
2
2
3
3

inpput
3
output
3

input
9991
output
97
103
'''
