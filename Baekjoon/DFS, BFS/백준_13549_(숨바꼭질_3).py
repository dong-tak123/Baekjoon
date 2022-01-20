# -*- coding: utf-8 -*-
"""백준 13549 (숨바꼭질 3)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jWJZHKdVlYnAv-SNHcOKdyCzPtQzdVAm

순간이동 *2될 때는 시간이 안 든다..

-> 2 * rear를 가장 먼저 확인 해준다!
"""

from collections import deque

def bfs(start, dist, k):
    queue = deque([start])
    while queue:
        rear = queue.popleft()

        #목적지면 종료
        #목적지랑 출발지가 같으면 여기서 바로 0으로 끝난다..
        if rear == k:
            print(dist[k])
            break
        
        #시작점부터 1초 뒤에 갈 수 있는 곳에 대해서 계속 거리를 늘려줌
        # 
        for i in (2*rear, rear-1, rear+1):
            #print(i)
            #중복해서 더해질수도 있으니까 계산이 안되어있던 점을 추가해 줘야함..
            if (0 <= i <= max) and (dist[i] == 0):
                queue.append(i)
                if i == 2*rear:
                    dist[i] = dist[rear]
                else:
                    dist[i] = dist[rear] + 1

max = 100000
n, k = map(int, input().split())

dist = [0] * (max+1)

bfs(n, dist, k)