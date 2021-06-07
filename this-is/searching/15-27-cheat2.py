# 문제 의도는 이진탐색을 쓰는 것이지만, Counter class 사용하는 법도 있음
from collections import Counter

n, x = map(int, input().split())
array = list(map(int, input().split()))
counter = Counter(array)
result = counter[x]
print(result) if result != 0 else print(-1)

'''
input
7 2 
1 1 2 2 2 2 3
output
4

input
7 4
1 1 2 2 2 2 3
output
-1
'''
