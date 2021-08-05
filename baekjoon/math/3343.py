# https://www.acmicpc.net/problem/3343
n, bunch1, cost1, bunch2, cost2 = map(int, input().split())

if bunch1 < bunch2:
    bunch1, bunch2 = bunch2, bunch1
    cost1, cost2 = cost2, cost1

num1 = n // bunch1
if n % bunch1 != 0:
    num1 += 1

prev_cost = int(1e9)
cur_cost = cost1 * num1
while prev_cost >= cur_cost:
    prev_cost = cur_cost
    num1 -= 1
    remain = n - num1 * bunch1
    num2 = remain // bunch2
    if remain % bunch2 != 0:
        num2 += 1
    cur_cost = num1 * cost1 + num2 * cost2

print(prev_cost)

'''
input
22 2 3 10 14
output
31
'''
