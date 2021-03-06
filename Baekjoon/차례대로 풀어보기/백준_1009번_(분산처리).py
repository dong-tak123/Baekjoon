# -*- coding: utf-8 -*-
"""백준 1009번 (분산처리)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G_SMJL4RXVegVfPpZ7T9gWktjiL3L2qC

**문제**

- 데이터 $a^b$ 개를 10대의 컴퓨터에 분산처리..
- 마지막 데이터는 누가 처리하는지 출력

**풀이**

- 각 1의 자리수마다 순환함...
- 0 : 1, 1 : 1, 2 : 4, 3 : 4, 4 : 2, 5 : 1, 6 : 1, 7 : 4, 8 : 4, 9 : 2
"""

T = int(input())
last = {0 : [10], 1 : [1], 2 : [6,2,4,8], 3 : [1,3,9,7], 4 : [6,4], 5 : [5],
        6 : [6], 7 : [1,7,9,3], 8 : [6,8,4,2], 9 : [1,9]}

for _ in range(T):
    a,b = map(int, input().split())
    a %= 10
    b = b % len(last[a])
    print(last[a][b])

