# 활용 예2)정렬된 두 리스트의 합집합
# 교과서 풀이랑은 좀 다름
n, m = 3, 4  # 각각의 리스트의 크기
a = [1, 3, 5]
b = [2, 4, 6, 8]

result = []

idx_a, idx_b = 0, 0
for _ in range(n + m):
    if idx_b >= m or (idx_a < n and a[idx_a] < b[idx_b]):
        result.append(a[idx_a])
        idx_a += 1
    else:
        result.append(b[idx_b])
        idx_b += 1

print(result)
