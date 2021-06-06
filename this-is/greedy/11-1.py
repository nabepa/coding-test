n = int(input())
fears = list(map(int, input().split()))
fears.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for fear in fears:
    count += 1
    if count >= fear:
        result += 1
        count = 0

print(result)

'''
input1
5
2 3 1 2 2
output1
2
'''
