# https://www.acmicpc.net/problem/20300
# 서강근육맨
n = int(input())
array = list(map(int, input().split()))

array.sort()

max_val = 0
if len(array) % 2 == 1:
    max_val = array.pop()

length = len(array)
for i in range(length // 2):
    sum_val = array[i] + array[length - 1 - i]
    max_val = max(max_val, sum_val)

print(max_val)

'''
input
5
1 2 3 4 5
output
5
'''
