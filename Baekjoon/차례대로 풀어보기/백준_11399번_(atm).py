# -*- coding: utf-8 -*-
"""백준 11399번 (ATM)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gn6UjhvhPFl286G3lxwz5pKoY7khGB9_

**문제**

- N명이 돈을 뽑는데, ATM기기가 한대다
- 모든 사람이 돈뽑는데 걸리는 시간의 합의 최솟값을 구하라

**풀이**

- 젤 빨리 뽑을 수 있는 사람이 먼저 뽑으면 된다..
"""

N = int(input())
time = list(map(int, input().split()))

time.sort()
sum = 0
for i, t in enumerate(time):
    sum += (N-i)*t

print(sum)

