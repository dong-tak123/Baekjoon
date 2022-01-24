# -*- coding: utf-8 -*-
"""케빈 베이컨의 6단계 법칙

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bbeN6J96TgWpE7Iy7Hj6IbJYTCyzfyWj
"""

from collections import deque

n, m = map(int, input().split())

def bfs(i, n):
    #나머지 사람에게로 가는 최소 거리를 구하면 된다..
    kevin = [0] * (n+1)
    visited = set()
    q = deque()
    q.append(i)
    visited.add(i)

    while q:
        rear = q.popleft()
        for r in graph[rear]:
            if r not in visited:
                q.append(r)
                visited.add(r)
                kevin[r] = kevin[rear] + 1
    return sum(kevin)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)

result = []
#모든 사람에 대해 bfs를 실시
for i in range(1, n+1):
    result.append(bfs(i, n))

tmp = min(result)
print(result.index(tmp) + 1)