import sys
input = sys.stdin.readline

n = int(input())
histogram = []
for _ in range(n):
    histogram.append(int(input()))


def solution(start, end):
    mid = (start + end) // 2
    left, right = mid - 1, mid + 1
    if left < start and right >= end:
        return 0

    max_val = histogram[mid]
    y = max_val
    for x in range(2, end - start + 1):
        if left < 0:
            y = min(y, histogram[right])
            right += 1
        elif right >= end:
            y = min(y, histogram[left])
            left -= 1
        elif histogram[left] > histogram[right]:
            y = min(y, histogram[left])
            left -= 1
        else:
            y = min(y, histogram[right])
            right += 1
        max_val = max(max_val, x * y)
        x += 1
    return max(max_val, solution(start, mid - 1), solution(mid + 1, end))


print(solution(0, n))

'''
input
7
2
1
4
5
1
3
3
output
8
'''
