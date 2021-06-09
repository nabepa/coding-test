# https://www.acmicpc.net/problem/2965

a, b, c = map(int, input().split())

cnt = 0
while True:
    left = b - a
    right = c - b

    if left == right == 1:
        break
    elif left > right:
        c, b = b, b - 1
    else:
        a, b = b, b + 1
    cnt += 1

print(cnt)

'''
input
3 5 9
output
3
'''
