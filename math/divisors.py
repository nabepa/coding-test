# 자연수의 모든 약수 찾기
# Find all divisors of a natural number

# 모든 약수는 짝을 이름
# eg. if n = 100 then (1,100), (2,50), (4,25), (5,20), (10,10)

# https://www.geeksforgeeks.org/find-divisors-natural-number-set-1/
import math


def find_divisors(n):
    divisors = []
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:  # pair of same value
            pair = n // i
            if pair == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(pair)
        i += 1

    return divisors


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


if __name__ == '__main__':
    n = int(input())
    # print(find_divisors(n))
    print(find_divisors_with_sort(n))
