# -*- coding: utf-8 -*-
"""백준 13199 (치킨 먹고 싶다)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jkSvvyn_-bnCOSHLcA-9GE5z0ROqjBVK

**문제**

- 1회 시킬 때 마다 쿠폰 C개
- 공짜로 시킬때 쿠폰 F개 사용
- 상언이는 쿠폰 사용할 때도 쿠폰을 받을 수 있음
- 두영이는 쿠폰 사용할 때는 쿠폰 못 받음
- 상언이가 두영이보다 몇개 더 먹을 수 있나?

**풀이**

- 시간이 1초라 반복문이 있으면 때려 죽여도 안된다..
- 결국 수학적으로 계산해야 한다.
- 상언이가 실제로 쿠폰으로 먹을때 사용하는 쿠폰을 (F - C)개라는 것을 착안한다.
- 하지만 그냥 (F-C)로 나눈 몫을 계산해버리면 오차가 난다
- 일단 한개 먹었다 치고 그 다음부터 위와 같이 계산한다
"""

#한마리씩 더 먹는다고 생각하자..

T = int(input())

for _ in range(T):
    P, M, F, C = map(int, input().split())

    #두사람이 받는 전체 쿠폰 갯수
    coupon_num = (M//P) * C

    #두영이는 그래도 고정
    doyoung = coupon_num // F

    sangun = 0
    #상언이가 한마리씩 더 먹는다 해보자..
    #처음에는 그냥 사먹고 그다음에 사먹을때부터 (F-C개 손해이다..)
    if coupon_num >= F:
        sangun = 1 + (coupon_num - F) // (F-C)
    
    print(sangun - doyoung)

#import sys 해도 시간 초과

T = int(input())

for _ in range(T):
    P, M, F, C = map(int, input().split())

    #두사람이 받는 전체 쿠폰 갯수
    coupon_num = (M//P) * C

    #두영이는 쿠폰으로 사면 그냥 끝이므로 더먹을수있는 치킨은 고정..
    doyoung = coupon_num // F
    
    #상언이는 쿠폰으로 사도 C개의 쿠폰줌
    #쿠폰으로 F로 나눈 몫을 계속 더하면 됨
    sangun = 0
    #애초에 나머지가 없으면 ...
    while (coupon_num // F > 0):
        sangun += coupon_num // F
        coupon_num = (coupon_num // F) * C + coupon_num % F

    print(sangun - doyoung)

