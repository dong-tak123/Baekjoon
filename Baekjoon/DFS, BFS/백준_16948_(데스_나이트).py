# -*- coding: utf-8 -*-
"""백준 16948 (데스 나이트)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16-felFW6Cm1T6HDYUoYXK9zUgiZUHFO6

- 이동할 수 있는 경우의 수를 모두 거리를 visited에 체크하면서 방문한다

- 목적지에 간적이 있으면 해당 거리를 출력한다
"""

from collections import deque

def bfs():
    q = deque()
    q.append([sx, sy])

    while q:
        tx, ty = q.popleft()
        for i in range(6):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0<=nx<n and 0<=ny<n and (visited[nx][ny]==0):
                q.append([nx, ny])
                visited[nx][ny] = visited[tx][ty] + 1

n = int(input())
visited = [[0]*n for _ in range(n)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

sx, sy, gx, gy = map(int, input().split())

bfs()

if visited[gx][gy]:
    print(visited[gx][gy])
else:
    print(-1)