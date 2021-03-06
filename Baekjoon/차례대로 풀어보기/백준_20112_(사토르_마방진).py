# -*- coding: utf-8 -*-
"""백준 20112 (사토르 마방진)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hgksXOlWNdE3nHRHPOlPK6QiH9LOsAR8

**풀이**

- 주어진 행렬이 Symmetric이면 된다..
"""

N = int(input())

is_mabangjin = True
words = []
for _ in range(N):
    words.append(input())

for i in range(N):
    for j in range(1, N):
        if words[i][j] != words[j][i]:
            is_mabangjin = False
            break
        j += 1

if is_mabangjin:
    print("YES")
else:
    print("NO")