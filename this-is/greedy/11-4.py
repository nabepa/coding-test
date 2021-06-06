# need to review: good idea!
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

tar = 1
for coin in coins:
    if tar < coin:
        break
    tar += coin

print(tar)
