# https://www.acmicpc.net/problem/6549
# 1725랑 같은 문제, 입력 형태만 다르고 완전 동일
import sys
input = sys.stdin.readline


def solution(histogram, start, end):
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
    return max(max_val, solution(histogram, start, mid - 1), solution(histogram, mid + 1, end))


while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    n = data[0]
    result = solution(data[1:], 0, n)
    print(result)


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
