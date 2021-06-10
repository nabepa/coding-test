# https://www.acmicpc.net/problem/11005
# 진법 변환 2
# 10진법 -> b 진법

NUM = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def transform_notation_from_dec(n, b):
    if n < b:
        return NUM[n]
    else:
        return transform_notation_from_dec(n // b, b) + NUM[n % b]


n, b = map(int, input().split())  # 10진법 n을 b진법으로 변환
print(transform_notation_from_dec(n, b))

'''
input
60466175 36
output
ZZZZZ
'''
