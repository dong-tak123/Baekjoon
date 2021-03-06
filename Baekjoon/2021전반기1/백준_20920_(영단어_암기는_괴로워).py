# -*- coding: utf-8 -*-
"""백준 20920 (영단어 암기는 괴로워)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eWk_1l1qdkZF94jfvZ6q9UYGrIM745tU

**문제**

- 우선순위 대로 단어를 정렬한다
    - 1. 자주 나오는 단어일수록 앞에 배치
    - 2. 길이가 길수록 앞에 배치
    - 3. 사전 순으로 앞에 있을수록 앞에 배치

**풀이**

- 딕셔너리 자료구조를 이용한다
- 키값에 실제 영단어, 밸류값에 나온 횟수, 길이, 알파벳 순서를 리스트로 저장한다
- 오름차순으로 정렬할 때 나온 횟수가 많을수록, 길이가 길수록 앞에 있으려면 저장할 때 반대로 저장해야 한다

**중요포인트**

- sorted()함수의 사용횟수를 어떻게 하면 줄이는가..
- 딕셔너리의 밸류에 관련된 모든 정보를 리스트로 넣고, 모두 오름차순으로 하면 알맞게 정렬되도록 적절히 수를 변형한다
"""

N, M = map(int, input().split())

#Note 딕셔너리의 value값에 나온 횟수, 길이, 알파벳을 리스트로 저장한다 
#오름차순으로 정렬할 때 나온 횟수가 많을수록, 길이가 길수록 앞에 있으려면
#저장할 때 반대로 저장해야 한다

Note = {}
for i in range(N):
    word = input()
    if len(word) >= M :         #M이상인 단어만 추가...
        if word in Note :
            Note[word][0] -= 1
        else :
            Note[word] = [-1, -len(word), word]

Notes = sorted(Note.values(), key = lambda x: (x[0], x[1], x[2]))

for i in Notes:
    print(i[2])

"""**트리 자료구조를 이용**

- heapq.heapify()사용...
- 메모리는 적긴한데 시간은 조금 더 길다..

**딕셔너리의 get()함수**

- 딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 할 수 있다
- get('a', 0) : 'a'라는 키가 없을 경우 0을 가져온다
"""

import heapq

n, m = map(int, input().split())
note = {}
for _ in range(n):
    word = input()
    length = len(word)
    if length >= m:
        #딕셔너리.get(key)함수,, : key가 있으면 반환, 없으면 그냥 넘어감
        #get(key, 기본값) : 있으면 반환, 없으면 기본값 반환
        note[word] = note.get(word, 0)+1

wordList = []

#노트의 아이템에서 우선순위에 맞도록 wordList 리스트에 추가한다..
for key, value in note.items():
    wordList.append((-value, -len(key), key))

#힙으로 O(n)시간에 바꾼다..
heapq.heapify(wordList)

#print(wordList)

while wordList:
    print(heapq.heappop(wordList)[2])

"""
sorted()함수의 무분별한 사용 -> 시간초과..
"""

N, M = map(int, input().split())

result = []
Note = {}
for i in range(N):
    word = input()
    if len(word) >= M :         #M이상인 단어만 추가...
        if word in Note :
            Note[word] += 1
        else :
            Note[word] = 1

Note = sorted(Note.items(), key=lambda x : x[1], reverse = True)        #리스트로 반환(나온횟수로 정렬)
#많이 나온 게 앞에있음

# 새로운 리스트 생성..
count = 0
last = []
for i in range(len(Note)):
    if i == 0:
        last.append([])
        last[count].append(Note[i][0])
    else :
        if Note[i][1] == Note[i-1][1]:
            last[count].append(Note[i][0])
        else :
            count += 1
            last.append([])
            last[count].append(Note[i][0])
#last라는 리스트에 나오는 횟수가 같은 것끼리 리스트로 묶여서 저장되어있다..
#나오는 횟수가 작은순서대로.. 리스트의 리스트안에서는 순서는 없음..

for i in range(len(last)):
    last[i] = sorted(last[i], key = lambda x:len(x), reverse = True)
    
for i in range(len(last)):
    for j in range(len(last[i])):
        print(last[i][j])