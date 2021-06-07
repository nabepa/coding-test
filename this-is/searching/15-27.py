def bisect_start(array, x):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == x and (mid == 0 or x > array[mid - 1]):
            return mid
        elif array[mid] >= x:
            end = mid - 1
        else:
            start = mid + 1

    return None


def bisect_end(array, x):
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == x and (mid == len(array) - 1 or x < array[mid + 1]):
            return mid
        elif array[mid] > x:
            end = mid - 1
        else:
            start = mid + 1

    return None


def count_by_range(array, a, b):
    left = bisect_start(array, a)
    if left == None:
        return 0

    right = bisect_end(array, b)
    return right - left + 1


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
