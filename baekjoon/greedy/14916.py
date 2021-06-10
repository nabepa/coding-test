n = int(input())

sum_val = 0
result = 0

cnt5 = n // 5
result = -1
for i in range(cnt5, -1, -1):
    sum_val = i * 5
    if sum_val == n:
        result = i
        break

    cnt2 = (n - sum_val) // 2
    sum_val += cnt2 * 2
    if sum_val == n:
        result = i + cnt2
        break

print(result)

'''
input
13
output
5

input
14
output
4
'''
