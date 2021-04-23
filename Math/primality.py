# 소수 판별
# Primality test
import math


# 주어진 수가 소수인지 판별
# 약수는 짝을 이루므로 루트 값까지 나누어 떨어지지 않으면, 그 이후도 나누어 떨어지지 않음
def check_primality(n):
    cnt = 0
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            cnt += 2
            if cnt > 2:
                break
        i += 1
    return True if cnt <= 2 else False


# n까지의 소수 찾기
# Find prime numbers until n
def find_prime_numbers(n):
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


if __name__ == '__main__':
    n = int(input())
    print(check_primality(n))
    print(find_prime_numbers(n))
