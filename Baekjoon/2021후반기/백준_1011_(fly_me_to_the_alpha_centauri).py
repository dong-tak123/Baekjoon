# -*- coding: utf-8 -*-
"""백준 1011 (Fly me to the Alpha Centauri)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1evkoN6dbSJjV6rRUWzOQiqAyTKpUqG5I

**문제**

- k광년 이동했을 때 다음에는 k-1, k, k+1 광년 중 하나를 이동할 수 있다
- 마지막 이동은 항상 1 이어야 한다
- 최소한의 작동횟수를 구하라

**풀이**

- 노가다 결과 1 2 3 3 4 4 5 5 5 6 6 6 7 7 7 7 8 8 8 8 ...
- 홀수가 나올때마다 하나씩 늘어나고, 홀수와 그 다음 짝수가 나오는 횟수는 같다..
- 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5 + 6
"""

def movement(N):
    i = 1
    while (i*(i+1) < N):
        i += 1
    #중심에 어디있는지 체크..
    if i*(i+1) - N >= i:
        print(2*i-1)
    else:
        print(2*i)

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    real_distance = y - x
    movement(real_distance)

"""**풀이**

- 1+2+3+4+3+2+1 -> 16($4^2$)..
- 1+2+3+4+5+4+3+2+1 -> 25($5^2$)..
- 이 제곱과의 관계를 생각해서 구한다..
"""

import math

N = int(input())

count = 0               # 최소 작동 횟수
result = []

for _ in range(N):
    x , y = map(int, input().split())
    distance = y - x
    
    num = math.floor(math.sqrt(distance))  # 주어진 값들 사이의 거리에 루트 씌움(제곱근)
    num_squared= num**2
    
    if distance == num_squared:
        count = (num*2) -1
    
    elif num_squared < distance <= num_squared + num:
        count = (num*2)
        
    elif (num_squared + num) < distance:
        count = (num*2) + 1
        
    elif distance < 4:
        count = distance
    result.append(count)
    
for x in result:
    print(x)