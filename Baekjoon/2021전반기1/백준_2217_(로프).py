# -*- coding: utf-8 -*-
"""백준 2217 (로프)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FXTowYvvHPQ-9Gc8m1PYeRSTsV-meyMN
"""

#import sys 하면 입력 시간 존나 줌..

N = int(input())

weight = []
for i in range(N):
    w = int(input())
    weight.append(w)

weight.sort(reverse = True)
capacity = weight[0]

for j in range(1,len(weight)):
    if weight[j] * (j+1) >= capacity:
        capacity = weight[j] * (j+1)
    else :
        pass

print(capacity)

10
2