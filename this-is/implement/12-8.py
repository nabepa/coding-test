data = input()

result = []
sum_val = 0
for a in data:
    if a.isalpha():
        result.append(a)
    else:
        sum_val += int(a)

result.sort()

if sum_val > 0:
    result.append(str(sum_val))

print(''.join(result))

'''
input
K1KA5CB7
output
ABCKK13

input
AJKDLSI412K4JSJ9D
output
ADDIJJJKKLSS20
'''
