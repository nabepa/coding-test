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


if __name__ == '__main__':
    n = int(input())
    print(check_primality(n))
