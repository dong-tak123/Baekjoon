# -*- coding: utf-8 -*-
"""백준 13116 (30번 문제)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hLd5A1yNrRaCYryjVZXorKfj0A5heGJB
"""

T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    path_a = [-1]
    path_b = [0.8]
    
    while a > 0:
        path_a.append(a)
        a = a // 2
    
    while b > 0:
        path_b.append(b)
        b = b // 2
    
    i = -1
    while 1:
        if (path_a[i] != path_b[i]):
            print(int(10*path_a[i+1]))
            break
        else :
            i -= 1

import sys

T = int(input())

for t in range(T):
    a, b = map(int, sys.stdin.readline().split())
    path_a = [-1]
    path_b = [0.8]
    
    while a > 0:
        path_a.append(a)
        a = a // 2
    
    while b > 0:
        path_b.append(b)
        b = b // 2
    
    i = -1
    while 1:
        if (path_a[i] != path_b[i]):
            print(int(10*path_a[i+1]))
            break
        else :
            i -= 1