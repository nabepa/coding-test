# 소수 판별
# Primality test
from math import sqrt, log, ceil


# 주어진 수가 소수인지 판별
# 약수는 짝을 이루므로 루트 값까지 나누어 떨어지지 않으면, 그 이후도 나누어 떨어지지 않음
# def check_primality(n):
#     if n == 1:
#         return False
#     cnt = 0
#     i = 1
#     while i <= sqrt(n):
#         if n % i == 0:
#             cnt += 2
#             if cnt > 2:
#                 break
#         i += 1
#     return True if cnt <= 2 else False
def check_primality(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    # n까지의 소수 찾기
    # Find prime numbers until n


def find_primes_until(n):
    array = [True for i in range(n + 1)]

    # Eratosthenes' sieve
    for i in range(2, int(sqrt(n)) + 1):
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


# n번째 소수
# n번째 소수가 있을 하한, 상한이 있음(prime number theorem)
# 상한값 까지의 소수를 Eratosthenes' sieve로 구하고, n번째 추출
# https://blog.naver.com/kyh941031/221634481228 참고
def find_nth_prime(n):
    if n < 6:
        primes = [2, 3, 5, 7, 11]
        return primes[n - 1]
    else:
        limit = ceil(n * log(n) + n * log(log(n)))
        primes = find_primes_until(limit)
        return primes[n - 1]


if __name__ == '__main__':
    n = int(input())
    print(check_primality(n))
    # print(find_primes_until(n))
    # print(find_nth_prime(n))7
