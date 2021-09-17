# -*- coding: utf-8 -*-
"""백준 10989 (수 정렬하기 3)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EKI85P6wyhS4UvIC82aPrkdJNL8EERPQ

**문제**

- 오름차순으로 정렬..
- 정렬해야하는 수가 천만개..
- 범위는 10000보다 작은 자연수..

**첫번째 풀이**

- 나올 때마다 딕셔너리에 횟수를 적어놓자..
- 딕셔너리를 한번 소트하자..
- 시간초과.. -> 재채점 후 통과..
"""

#시간초과..

N = int(input())
nums = {}
for _ in range(N):
    a = int(input())
    if a in nums:
        nums[a] += 1
    else:
        nums[a] = 1

nums = sorted(nums.items())
for i in range(len(nums)):
    for _ in range(nums[i][1]):
        print(nums[i][0])

"""**두번째 풀이**

- 그럼 리스트를 아예 10000개만 해놓고 하는 수밖에 없는데..
- 인덱스에서 -1 계산을 할 필요가 없도록 10001짜리의 리스트를 만들어도 됨
"""

N = int(input())

nums = [0] * 10001

#입력받은 횟수..
for _ in range(N):
    a = int(input())
    nums[a] += 1

#출력..
for i in range(1,10001):
    if nums[i]:
        for _ in range(nums[i]):
            print(i)

