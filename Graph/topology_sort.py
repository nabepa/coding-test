from collections import deque

v, e = map(int, input().split())  # len of vertex, edge
indegree = [0] * (v + 1)  # 모든 노드에 대한 진입차수, 0으로 초기화
graph = [[] for _ in range(v + 1)]  # 간선 정보를 담기 위한 인접 리스트 초기화

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # a -> b
    indegree[b] += 1  # 진입차수 1 증가


# Topology osrt
# 사이클 발생이 없다는 가정일 때의 알고리즘
def topology_sort():
    result = []  # 수행 결과를 담을 리스트
    q = deque()  # 큐

    # 시작 전에 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:  # 큐가 빌 때까지
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    for i in result:
        print(i, end=' ')
    print()


topology_sort()
