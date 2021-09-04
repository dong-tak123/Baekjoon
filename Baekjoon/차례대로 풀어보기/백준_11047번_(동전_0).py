# -*- coding: utf-8 -*-
"""백준 11047번 (동전 0)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1i2Kp7ZwGGtgh0BvXwmga6k0RTFpQk1X0

**문제**

- N, K가 주어짐..
- N개의 동전의 종류
- K원을 만들어야 함
- 필요한 최소 동전 수..

**풀이**

- 오름차순 입력이니까 젤 큰거부터 나눠가면서 확인..
"""

N, K = map(int, input().split())

coin = []
for _ in range(N):
    m = int(input())
    if m <= K:
        coin.append(m)
        
cnt = 0
i = -1
while K > 0:
    cnt += K // coin[i]
    K = K % coin[i]
    i -= 1
print(cnt)