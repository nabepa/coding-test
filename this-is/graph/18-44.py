# https://www.acmicpc.net/problem/2887
# pypy 제출
# Kruskal
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())

xs = []
ys = []
zs = []
for i in range(n):
    x, y, z = map(int, input().split())
    xs.append((x, i))
    ys.append((y, i))
    zs.append((z, i))

xs.sort()
ys.sort()
zs.sort()

edges = []
for i in range(n - 1):
    j = i + 1
    edges.append((xs[j][0] - xs[i][0], xs[i][1], xs[j][1]))
    edges.append((ys[j][0] - ys[i][0], ys[i][1], ys[j][1]))
    edges.append((zs[j][0] - zs[i][0], zs[i][1], zs[j][1]))

edges.sort()

parent = [i for i in range(n)]
result = 0

for cost, a, b in edges:
    if find_parent(parent, a) == find_parent(parent, b):
        continue
    union_parent(parent, a, b)
    result += cost

print(result)

'''
input
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
output
4
'''
