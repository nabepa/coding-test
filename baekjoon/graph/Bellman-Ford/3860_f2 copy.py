# https://www.acmicpc.net/problem/3860
from collections import deque
from copy import deepcopy

INF = float('inf')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def check_connection_with_goal(graph: dict, a: tuple, goal: tuple) -> bool:
    visited = {key: False for key in graph}
    visited[a] = True
    q = deque()
    q.append(a)
    while q:
        v = q.popleft()
        for i, _ in graph[v]:
            if i == goal:
                return True
            if not visited[i]:
                q.append(i)
                visited[i] = True
    return False


def solution():
    while True:
        w, h = map(int, input().split())  # w X h
        if w == 0:
            return

        start = (0, 0)
        goal = (w - 1, h - 1)

        board = [[0] * w for _ in range(h)]

        g = int(input())  # g: 묘비의 개수
        for _ in range(g):
            x, y = map(int, input().split())
            board[y][x] = INF

        graph = {}
        e = int(input())  # e: 구멍의 개수
        for _ in range(e):
            x1, y1, x2, y2, t = map(int, input().split())
            board[y1][x1] = 1
            graph[(x1, y1)] = [((x2, y2), t)]

        for y in range(h):
            for x in range(w):
                if board[y][x] != 0:
                    continue
                graph[(x, y)] = []
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if ny < 0 or ny >= h or nx < 0 or nx >= w or board[ny][nx] == INF:
                        continue
                    graph[(x, y)].append(((nx, ny), 1))

        v = len(graph)
        dist = {key: INF for key in graph}
        dist[start] = 0

        negative_checker = {key: 0 for key in graph}

        q = deque()
        q.append(start)
        while q:
            a = q.popleft()
            for b, cost in graph[a]:
                temp = dist[a] + cost
                if dist[b] > temp:
                    dist[b] = temp
                    if b not in q:
                        q.append(b)
                        negative_checker[b] += 1
                        if negative_checker[b] > v:
                            break

        is_loop = False
        for key, edges in graph.items():
            a = key
            for b, cost in edges:
                temp = dist[a] + cost
                if dist[b] > temp:
                    if check_connection_with_goal(graph, b, goal):
                        is_loop = True
                        break

        if dist[goal] == INF:
            print('Impossible')
        elif is_loop:
            print('Never')
        else:
            print(dist[goal])


if __name__ == '__main__':
    solution()
