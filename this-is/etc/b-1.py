# p.485
# https://www.acmicpc.net/problem/1929
from math import sqrt
m, n = map(int, input().split())

table = [True] * (n + 1)
table[0], table[1] = False, False
for i in range(2, int(sqrt(n)) + 1):
    if table[i]:
        for j in range(2 * i, n + 1, i):
            table[j] = False

for i in range(m, n + 1):
    if table[i]:
        print(i)

'''
intput
3 16
output
3
5
7
11
13
'''
