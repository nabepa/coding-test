# https://www.acmicpc.net/problem/1110
# 더하기 사이클
n = input()

transfered = n
cnt = 0

while True:
    if len(transfered) == 1:
        transfered = '0' + transfered

    sum_val = sum(map(int, transfered))
    sum_val = str(sum_val)
    if len(sum_val) == 1:
        sum_val = '0' + sum_val

    transfered = transfered[1] + sum_val[1]

    cnt += 1

    # transfered가 1자리일때 앞에 0을 붙이지 않은 반면, n은 한자리여도 앞에 0 안 붙였으므로
    # 이때를 대비해 int로 만들어 비교
    if int(transfered) == int(n):
        break

print(cnt)

'''
input
26
output
4

input
55
output
3

input
1
output
60

input
0
output
1
'''
