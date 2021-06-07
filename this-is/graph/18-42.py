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


g = int(input())
p = int(input())

result = 0
parent = [i for i in range(g + 1)]
for i in range(p):
    info = int(input())  # 들어 온 비행기 정보
    gate = find_parent(parent, info)  # 비행기를 도킹할 게이트 번호
    if gate == 0:  # 도킹할 게이트 번호로 0이 반환됬다는 것은 더 이상 도킹할 곳이 없다는 것
        break
    union_parent(parent, gate, gate - 1)
    result += 1

print(result)

'''
input
4
3
4
1
1
output
2
'''
