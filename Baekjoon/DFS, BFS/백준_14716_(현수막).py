# -*- coding: utf-8 -*-
"""백준 14716 (현수막)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GM2KvMTVf1QCf282R68-BpcV8Yn-ISFU
"""

#대각선 까지 연결된 것으로 봄
from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x, y])
    board[x][y] = 0
    while q:
        tx, ty = q.popleft()
        for p in range(8):
            nx = tx + dx[p]
            ny = ty + dy[p]
            if (0<=nx<row) and (0<=ny<col) and board[nx][ny]:
                q.append([nx, ny])
                board[nx][ny] = 0

row, col = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(row)]
dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, 0, -1, 1, 0, -1, 1, -1]

cnt = 0
for i in range(row):
    for j in range(col):
        if board[i][j] == 1:
            bfs(i, j)
            cnt += 1

print(cnt)