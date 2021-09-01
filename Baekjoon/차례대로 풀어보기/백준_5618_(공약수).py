# -*- coding: utf-8 -*-
"""백준 5618 (공약수)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bLubX2MOFElLipLpZ2Zn_DWFuzIsobcc

**문제**

- 자연수 n개가 주어지고, 그 수들의 공약수를 모두 구하라
- 입력의 갯수는 2 또는 3이다

**풀이**

- 최대공약수를 구하고 약수를 출력..
- import sys 해도 시간 초과가 돼서 pypy로 했다..
"""

def GCD(a, b):
    while (b > 0):
        a,b = b, a%b
    return a

N = int(input())
nums = list(map(int, input().split()))

if N == 2:
    gcd = GCD(nums[0], nums[1])
else:
    gcd = GCD(nums[0], GCD(nums[1], nums[2]))

for i in range(1, gcd//2 + 1):
    if gcd % i == 0:
        print(i)
print(gcd)