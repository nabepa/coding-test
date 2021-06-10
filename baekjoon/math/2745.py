# https://www.acmicpc.net/problem/2745
# 진법 변환 b 진법 -> 10진법

def transform_alpha_to_dec(s):
    return ord(s) - ord('A') + 10


n, b = input().split()  # b 진법수 n
b = int(b)
result = 0

# (result + 아직 더하지 않은 것중 제일 높은 자리수) * b를 반복
for d in n:
    result *= b
    if d.isalpha():
        result += transform_alpha_to_dec(d)
    else:
        result += int(d)

print(result)

'''
input
ZZZZZ 36
output
60466175
'''
