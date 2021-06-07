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


n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

parent = [i for i in range(n + 1)]
for i in range(n):
    for j in range(i + 1, n):
        if graph[i][j] == 1:
            union_parent(parent, i + 1, j + 1)

b_dif = True
common_parent = find_parent(parent, plan[0])
for p in plan[1:]:
    if find_parent(parent, p) != common_parent:
        b_dif = False
        break

print('YES') if b_dif else print('NO')

'''
input
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
output
YES
'''
