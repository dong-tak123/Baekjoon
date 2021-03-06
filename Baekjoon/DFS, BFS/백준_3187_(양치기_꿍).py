# -*- coding: utf-8 -*-
"""백준 3187 (양치기 꿍)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pGeuD7FbzDJa5f1vLdLrf8nif6S5BPC2

매 bfs마다 늑대와 양의 마리수를 구해서 누가 잡아먹히는지를 반환한다
"""

from collections import deque

def bfs(x, y):
    q = deque()
    q.append([i, j])
    wolves, sheep = 0, 0
    while q:
        tx, ty = q.popleft()
        if field[tx][ty] == 'v':
            wolves += 1
        elif field[tx][ty] == 'k':
            sheep += 1
        visited[tx][ty] = True

        for p in range(4):
            nx = tx + dx[p]
            ny = ty + dy[p]

            if (0<=nx<row) and (0<=ny<col):
                if (not visited[nx][ny]) and (field[nx][ny] != '#'):
                    visited[nx][ny] = True
                    q.append([nx, ny])
    #print(wolves, sheep)
    if wolves < sheep:
        return 0, sheep
    else:
        return wolves, 0


row, col = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
field = []
visited = [[False] * col for _ in range(row)]
w_cnt, s_cnt = 0, 0

for _ in range(row):
    field.append(list(input()))
        
for i in range(row):
    for j in range(col):
        if (field[i][j] != '#') and (not visited[i][j]):
            a, b = bfs(i, j)
            w_cnt += a
            s_cnt += b

print(s_cnt, w_cnt)

"""
9 12
.###.#####..
#.kk#...#v#.
#..k#.#.#.#.
#..##k#...#.
#.#v#k###.#.
#..#v#....#.
#...v#v####.
.####.#vv.k#
.......####.

3 5
"""