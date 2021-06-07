n = int(input())
array = list(map(int, input().split()))

result = -1
start = 0
end = n - 1
while start <= end:
    mid = (start + end) // 2
    if array[mid] == mid:
        result = mid
        break
    elif array[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1

print(result)

'''
input
5
-15 -6 1 3 7
output
3

input
7
-15 -4 2 8 9 13 15
output
2

input
7
-15 -4 3 8 9 13 15
output
-1
'''
