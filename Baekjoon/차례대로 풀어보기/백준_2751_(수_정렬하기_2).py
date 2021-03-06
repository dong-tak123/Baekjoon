# -*- coding: utf-8 -*-
"""백준 2751 (수 정렬하기 2)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14ndeIOC8bB-ig9jcKAvQtSrcisSj05HL

- 시간 복잡도가 O(nlogn)인 정렬 알고리즘으로 풀 수 있습니다. 
- 예를 들면 병합 정렬, 힙 정렬 등이 있지만, 어려운 알고리즘이므로 지금은 언어에 내장된 정렬 함수를 쓰는 것을 추천드립니다.

**풀이**

- heapq모듈을 이용한다
- 다 입력을 받고 heapq.heapify()를 이용해서 힙으로 만든다
- heapq.heappop()을 이용해서 작은 거부터 출력한다
"""

import heapq

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

heapq.heapify(nums)

for _ in range(N):
    print(heapq.heappop(nums))

