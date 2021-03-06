# -*- coding: utf-8 -*-
"""백준 1026 (보물)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CyXpI_oH8Hir6UFFI7gI5TjZ7uZtbiCb

A만 위치를 바꿀수 있다고 문제에는 나와있지만 사실 B도 위치를 바꿔도 된다..

최솟값을 만들어내야하므로 A의 최소에 B의 최대가 곱해지도록 만들어야 하는게 key point이다
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort()

sum = 0
for i in range(N):
    sum += A[i]*B[i]
print(sum)