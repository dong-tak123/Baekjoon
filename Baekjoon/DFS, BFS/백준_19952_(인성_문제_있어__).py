# -*- coding: utf-8 -*-
"""백준 19952 (인성 문제 있어??)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J1OvrUjAf2lQqXEz4LKXYzXCI1uaMJDT
"""

from collections import deque
def bfs(x, y, GX, GY, f):
    q = deque()
    q.append([x,y,f])       #현재 남은 힘도 저장함
    visited[x][y] = True
    while q:
        tx, ty, tf = q.popleft()
        if tx == GX and ty == GY:
            print("잘했어!!")
            return
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            # 남은 힘이 0이하이면 더이상 이동 불가
            if tf == 0:
                continue
            
            # 움직일 수 있으면
            if 0<=nx<row and 0<=ny<col and not visited[nx][ny]:
                if (graph[nx][ny]-graph[tx][ty]) <= tf:
                    q.append([nx, ny, tf-1])
                    visited[nx][ny] = True
    print("인성 문제있어??")

t = int(input())
for _ in range(t):
    row, col, o, f, sx, sy, gx, gy = map(int, input().split())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    graph = [[0] * col for _ in range(row)]
    visited = [[False] * col for _ in range(row)]

    for _ in range(o):
        X, Y, n = map(int, input().split())
        graph[X-1][Y-1] = n

    bfs(sx-1, sy-1, gx-1, gy-1, f)