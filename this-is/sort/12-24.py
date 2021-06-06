# https://www.acmicpc.net/problem/18310
n = int(input())
homes = list(map(int, input().split()))
homes.sort()

print(homes[(n - 1) // 2])  # median

'''
input
4
5 1 7 9
output
5
'''
