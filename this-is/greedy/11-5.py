n, m = map(int, input().split())
balls = list(map(int, input().split()))

cnt = [0] * (m + 1)  # number of each ball
for ball in balls:
    cnt[ball] += 1

result = 0
for i in range(1, m + 1):
    n -= cnt[i]
    result += cnt[i] * n

print(result)
