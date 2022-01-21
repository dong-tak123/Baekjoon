# -*- coding: utf-8 -*-
"""백준 13565 (침투)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eU4iVTTqwJRzQr8XTmnalrfL7P4db6Gq

outer side에서 dfs를 수행한다

inner side에서 체크 되었는지 확인한다

계속 recursionError
"""

"""
import sys
sys.setrecursionlimit(1000000)      #아예 10**6 정도로 키워버린다
input = sys.stdin.readline
"""

def dfs(row, col):
    matrix[row][col] = 2
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for p in range(4):
        nrow = row + dx[p]
        ncol = col + dy[p]
        
        if (0 <= nrow < m) and (0 <= ncol < n):
            if (matrix[nrow][ncol] == 0):
                dfs(nrow, ncol)

# m 가로, n 세로
m, n = map(int, input().split())

matrix = []
for _ in range(m):
    matrix.append(list(map(int, list(input()))))

#outer side에서 0인 부분에서만 시작한다
for col in range(n):
    if matrix[0][col] == 0:
        dfs(0, col)

#print(matrix)

#inner side에서 체크된 적이 있으면 YES
if 2 in matrix[-1]:
    print("YES")
else:
    print("NO")