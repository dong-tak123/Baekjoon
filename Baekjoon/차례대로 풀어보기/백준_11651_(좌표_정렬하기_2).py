# -*- coding: utf-8 -*-
"""백준 11651 (좌표 정렬하기 2)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p9d0v23wafsTOw5anXqtNohKOlth6AxN

**문제**

- y좌표, x좌표가 증가하는 순서로 정렬후 출력..
"""

N = int(input())
points = []
for _ in range(N):
    a, b = map(int, input().split())
    points.append([a,b])

#0번째 열, 1번째 열 (x, y) 순서로 정렬하자..
points_sorted = sorted(points, key = lambda x:(x[1],x[0]))

for i in range(N):
    print(points_sorted[i][0], points_sorted[i][1])

