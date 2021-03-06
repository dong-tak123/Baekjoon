# -*- coding: utf-8 -*-
"""백준 1057번(토너먼트)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s7XtAUSQXTh3XKnDQOEaSq9vZzImE2Fu

**문제**

- N명이 참가하는 토너먼트
- 인접한 사람끼리 경기..
- 둘이 붙는 라운드는..?

**풀이**

- 몇 번 포트에 있는지가 중요하다..
- 경기를 이기고 올라갔을 때, 다음 포트가 같다면 반복을 멈춘다..
- 다음 포트 계산법
    - 홀수 번일 때 : (n + 1) // 2
    - 짝수 번일 때 : n // 2
"""

N, a, b = map(int, input().split())

round = 1

while True:
    if a % 2 == 1:
        a += 1
    if b % 2 == 1:
        b += 1
    if a == b:
        break
    a = a // 2
    b = b // 2
    round += 1

print(round)

