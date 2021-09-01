# -*- coding: utf-8 -*-
"""백준 6603 (로또)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13D1zbsHZTpySdKGufV2zur4qCPcwMlTv

**문제**

- 번호가 k개 주어진다
- 그 중에서 6개를 고르는 방법을 모두 구해라
"""

from itertools import combinations

num = list(map(int, input().split()))

while num[0] != 0:
    possible_lotto = list(combinations(num[1:], 6))
    for i in possible_lotto:
        for j in i:
            print(j, end=" ")
        print()

    print()
    num = list(map(int, input().split()))



