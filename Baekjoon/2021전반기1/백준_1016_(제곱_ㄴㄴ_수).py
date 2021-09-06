# -*- coding: utf-8 -*-
"""백준 1016 (제곱 ㄴㄴ 수)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15Obj0M7-vuVH-nx2cvIF0LEpQ3uFWrVq

**문제**

- min, max 사이의 제곱수의 배수가 아닌 정수의 갯수를 구하라

**풀이**

- 메모리 초과 방지
    - min, max 사이의 크기만큼 dp를 만든다..

- 그다음 2의 제곱의 배수부터 지워나간다..
    - 지워야하는 첫번째 배수가 어딘지 찾기 위해 j = min // square를 수행한다..
    - 더불어서 시간초과를 방지한다
- 인덱싱은 min을 빼주면 된다
- 마지막에는 전체에서 제곱수의 배수인 것을 빼주면 된다..
"""

#[min, max]크기의 리스트를 선언하도록 해보자

min, max = map(int, input().split())

dp = [True] * (max-min+1)

i = 1
cnt = 0
# 2의 제곱의 배수부터 지워나가는데,,,
while i * i <= max:
    #1보다 큰 제곱수의 배수를 찾아야한다..
    i += 1
    square = i ** 2
    #일단 인덱스가 min과 max사이에 있어야..
    j = min // square   #얘부터 찾으면 된다..
    while square * j <= max:
        # 제곱의 배수의 인덱스가 min과 max사이에 있을 때
        if square*j - min >= 0 and dp[square*j - min]:
            #False로 바꾼다..
            cnt += 1
            dp[square*j - min] = False
        j += 1

#전체에서 뺀다..
print(len(dp) - cnt)

"""소수를 미리 만들어놓고 반복문 돌리는 것도 좋은 방법이다..

이게 훨씬 빠르다..
"""

#최대 범위 내의 소수를 잡아내는 함수..
def eratos(num):
    check = [False] * (num + 1)
    res = []
    for i in range(2, num + 1):
        if not check[i]:
            for j in range(2 * i, num + 1, i):
                check[j] = True
    for i in range(2, num + 1):
        if not check[i]:
            res.append(i)
    return res

a = eratos(1000000) #a에 1000000까지의 소수가 모여있음
n, m = map(int, input().split())
vis = [True] * (m - n + 1)
for i in a:     #소수들 중에서..
    start = n // (i ** 2)   #시간초과 방지책..
    for j in range(start * (i ** 2), m + 1, i ** 2):
        if n <= j <= m:     #돌리자..
            vis[j - n] = False
print(sum(vis))