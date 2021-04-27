from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:  # 큐가 빌 때까지
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 인접 리스트
graph = [
        [],  # 1번 노드의 정보를 index 1에 저장하기 위한 더미
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
]

# 방문 정보
visited = [False] * 9

bfs(graph, 1, visited)
print()
