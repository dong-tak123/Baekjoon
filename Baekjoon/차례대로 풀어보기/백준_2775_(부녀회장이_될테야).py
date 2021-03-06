# -*- coding: utf-8 -*-
"""백준 2775 (부녀회장이 될테야)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zO-xh8dav5zPJ-6vz1eud6Z0Ots-I_Wt

사람수를 표로 그려보면 규칙을 찾을 수 있다..

- 해당 층의 n호의 사람수를 구하려면 이전 층의 n호의 사람 수에서 해당 층의 n-1호의 사람수를 더하면 된다..
"""

#2775

T = int(input())
for i in range(T):
    k = int(input())    #층
    n = int(input())    #호
    member = [i for i in range(1, n+1)]
    for _ in range(k):
        for q in range(1, n):
            member[q] += member[q-1]
    print(member[-1])

