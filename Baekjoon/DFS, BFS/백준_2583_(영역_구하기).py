# -*- coding: utf-8 -*-
"""백준 2583 (영역 구하기)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IdWvoXLNO0igik_KaFcSJCdmHDz1O9WT

#문제

- 영역이 주어지는데 그 위에 눈금에 맞게 직사각형을 그린다

- 직사각형으로 나누어지는 영역의 넓이를 구해서 오름차순으로 정렬한다

#구현

- dfs구현 시 옆의 구역을 확인할 때마다 N을 1씩 증가시켜서 영역을 확인함
- sys.stdin.readline()을 이용해서 시간 단축
- sys.setrecursionlimit(100000) 사용해서 recursion error 방지
"""

#x, n가 col, y, m가 row

from collections import deque

def dfs(x, y):
    area[x][y] = 1
    N = 1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for p in range(4):
        nx = x + dx[p]
        ny = y + dy[p]

        if (0 <= nx < m) and (0 <= ny < n) and (area[nx][ny] == 0):
            N += dfs(nx, ny)
    return N

m, n, k = map(int, input().split())

area = [[0]*n for _ in range(m)]

for _ in range(k):
    x_l, y_l, x_u, y_u = map(int, input().split())
    for col in range(x_l, x_u):
        for row in range(y_l, y_u):
            area[row][col] = 1

res = []
for i in range(m):      #row
    for j in range(n):      #col
        size = 0
        if area[i][j] == 0:
            size = dfs(i, j)
        
        if size > 0:
            res.append(size)

res.sort()
print(len(res))
print(*(res))