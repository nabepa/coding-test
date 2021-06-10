# https://www.acmicpc.net/problem/5618
# 공약수
import math
n = int(input())
array = list(map(int, input().split()))
gcd = (math.gcd(*array))  # * 사용법 주목!


def find_divisors_with_sort(n):
    left = []
    right = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:  # pair of same value
            pair = n // i
            if pair == i:
                left.append(i)
            else:
                left.append(i)
                right.append(pair)
        i += 1

    right.reverse()

    return left + right


result = find_divisors_with_sort(gcd)
for r in result:
    print(r)

'''
input
2 75 125
output
1
5
25
'''
