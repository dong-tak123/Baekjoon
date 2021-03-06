# -*- coding: utf-8 -*-
"""백준 2577 (숫자의 개수)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ioE6wZWzKzQWe7iJfIpHRkcBNXgigrsd

세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하라

- 몇번 쓰였는지 알려주는 리스트를 하나 만든다
"""

count = [0] * 10

A = int(input())
B = int(input())
C = int(input())

num = A*B*C
while (num >0):
    count[num%10] += 1
    num = num // 10

for i in range(10):
    print(count[i])

