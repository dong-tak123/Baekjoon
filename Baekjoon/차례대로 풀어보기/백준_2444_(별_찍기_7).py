# -*- coding: utf-8 -*-
"""백준 2444 (별 찍기 - 7)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hwHQpBUOM7rYnNkL5Qu-AxNV3XPEPfam
"""

n = int(input())

for i in range(2*n - 1):
    if i < n:
        print(' '*(n-(i+1)) + '*'*(2*i+1))
    else:
        print(' '*((i+1)-n) + '*'*(2*(2*n-(i+1)) - 1))