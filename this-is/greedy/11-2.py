array = map(int, input())

result = 0
for num in array:
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
