# Count the number of frequencies of elements whose value is between [left, right] in a sorted array
from bisect import bisect_left, bisect_right


def count_by_range(array, left_val, right_val):
    right_idx = bisect_right(array, right_val)
    left_idx = bisect_left(array, left_val)
    return right_idx - left_idx


if __name__ == '__main__':
    array = list(map(int, input().split()))
    left, right = map(int, input().split())

    cnt = count_by_range(array, left, right)

    print(cnt) if cnt > 0 else print(-1)

'''
1 2 3 3 4 5
3 4
'''
