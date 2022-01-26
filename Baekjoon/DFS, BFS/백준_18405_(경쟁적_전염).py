# -*- coding: utf-8 -*-
"""백준 18405 (경쟁적 전염)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-H7CsjwKB3WcL-yKjSRxiwRCXxbmHbh9

1. 바이러스의 우선순위를 파악하기 위해 순위랑 위치를 함께 저장한다
2. 1초 당 갈 수 있는 위치에 모두 가야하기 때문에 그 시점의 queue의 길이만큼 모두 빼내서 확인해야 한다
"""

from collections import deque

n, k = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(S):
    q = deque(virus)
    s = 0   #초 세기
    while q:
        if s == S:
            break
        #1초에 우선순위에 맞춰서 모든 바이러스가 전파되어야 한다
        for p in range(len(q)):
            rank, tx, ty = q.popleft()        
            for i in range(4):
                nx = tx + dx[i]
                ny = ty + dy[i]
                if (0<=nx<n) and (0<=ny<n) and (graph[nx][ny]==0):
                    graph[nx][ny] = rank
                    q.append([rank, nx, ny])
        s += 1

graph = []
virus = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            #바이러스 번호와 위치를 함께 저장
            virus.append([graph[i][j], i, j])
S, GX, GY = map(int, input().split())

#바이러스 번호기준 오름차순 정렬
virus.sort()

bfs(S)

print(graph[GX-1][GY-1])