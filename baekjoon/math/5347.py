# https://www.acmicpc.net/problem/5347
# 라이브러리 사용하지 않은 풀이
for i in range(int(input())):
    num1, num2 = map(int, input().split())
    a, b = num1, num2
    # 유클리드 호제법을 이용한 최대 공약수(gcd)
    while a % b != 0:
        a, b = b, a % b  # b == gcd
    result = num1 * num2 // b
    print(result)

''' 
input
3
15 21
33 22
9 10
output
105
66
90
'''
