# https://www.acmicpc.net/submit/18406

data = list(map(int, input()))

half = len(data) // 2
left = sum(data[:half])
right = sum(data[half:])

print('LUCKY') if left == right else print('READY')

""" 
input1
123402
output1
LUCKY

input2
7755
output2
READY
"""