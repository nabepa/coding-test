from bisect import bisect_left, bisect_right


def count_by_range(array, a, b):
    left = bisect_left(array, a)
    right = bisect_right(array, b)
    return right - left


n, x = map(int, input().split())
array = list(map(int, input().split()))
result = count_by_range(array, x, x)
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
