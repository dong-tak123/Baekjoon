# -*- coding: utf-8 -*-
"""백준 9019 (DSLR)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HPCYoxupzXaDdEeOzF0Fq3aCSMNTg06J

연산

- D : 2n mod 10000
- S : n - 1
- L : 한칸 왼쪽으로
- R : 한칸 오른쪽으로

최소한의 명령어..

#시간 초과..

시간초과를 해결 방안
- visited를 set으로 지정하여 방문확인을 O(1)로 해준다
- L, R을 하는 함수를 따로 만든다

그래도 메모리 초과..
"""

from collections import deque

def left(n):
    a = n % 1000
    b = n // 1000
    return a * 10 + b

def right(n):
    a = n % 10
    b = n // 10
    return a * 1000 + b

def bfs(start, end):
    D = ['D', 'S', 'L', 'R']
    queue = deque()
    queue.append(start)
    while queue:
        rear = queue.popleft()
        if rear == end:
            print(graph[rear])
            break
        for d in D:
            if d == 'D':
                temp = (2*rear) % max
                if temp not in visited:
                    graph[temp] = graph[rear] + d
                    visited.add(temp)

            elif d == 'S':
                if rear == 0:
                    temp = 9999
                else:
                    temp = rear - 1
                    
                if temp not in visited:
                    graph[temp] = graph[rear] + d
                    visited.add(temp)

            elif d == 'L':
                temp = left(rear)
                if temp not in visited:
                    graph[temp] = graph[rear] + d
                    visited.add(temp)

            elif d == 'D':
                temp = right(rear)
                if temp not in visited:
                    graph[temp] = graph[rear] + d
                    visited.add(temp)
            queue.append(temp)
              
max = 10000
T = int(input())

for _ in range(T):
    graph = [''] * max
    visited = set()
    start, end = map(int, input().split())
    bfs(start, end)
