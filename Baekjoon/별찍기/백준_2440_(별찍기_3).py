# -*- coding: utf-8 -*-
"""백준 2440 (별찍기 - 3)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L_tna2cng_YX5kGnm7nvJPqoNsk-rcWa

첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍어라..
"""

N = int(input())

for i in range(N):
    print("*" * (N-i))

