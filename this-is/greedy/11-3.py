# need to review: good solution!
array = input()

cnt = [0, 0]
tar = array[0]
cnt[int(tar)] += 1

for a in array[1:]:
    if a != tar:
        tar = a
        cnt[int(a)] += 1


print(min(cnt))
