# -*- coding: utf-8 -*-
"""백준 1449 (수리공 항승)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ighcouMp5PXwRmh942XjVk4b76Yp9MaX

- N : 물이 새는 곳의 갯수
- L : 테이프 길이
- 새는 곳의 위치 입력..
"""

N, L = map(int, input().split())
a = list(map(int, input().split()))     #얘를 정렬해보자..
a.sort()

cnt = 1
start = a[0]
for i in range(1, len(a)):
    if (a[i] - start) <= L-1:   #한테이프로 최대한 많이 막아야함
        continue
    else:   #아니면 시작 누수부분 update..
        start = a[i]
        cnt += 1
print(cnt)