# https://www.acmicpc.net/problem/15649
from itertools import permutations

n, m = map(int, input().split())
array = [i for i in range(1, n + 1)]

result = list(permutations(array, m))
for row in result:
    for j in range(m):
        print(row[j], end=' ')
    print()
