# -*- coding: utf-8 -*-
"""백준 20116 (상자의 균형)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rpONS3WqXSe8gf07uq-qbuAgcQp44euA

**중요 포인트**

- 윗 상자들부터 쭉 더해가면서 내려온다
- 하나씩 더할 때마다 무게중심 평균을 내야지 시간초과 안 걸림
- 하다가 무게중심이 벗어나면 break!
"""

n, L = map(int, input().split())
center = list(map(int, input().split()))
stablity = True

#다 더하고 계산하지 말고, 더하는 도중에 break를 넣으면 좀 더 빠를거 같다..
#위에서 부터 계산해서 내려오면서 더해나감..
sum = 0
for i in range(n-1, 0, -1):     #내려오면서.. i = 1까지..
    sum += center[i]
    avg = sum / (n - i)     #하나를 더할때마다 무게 중심을 잰다..

    #위의 무게중심의 평균이 밑에거를 벗어나 있으면 break..
    if abs(avg - center[i-1]) >= L:
        stablity = False
        break

if stablity:
    print("stable")
else :
    print("unstable")

#틀림..

n, L = map(int, input().split())
center = list(map(int, input().split()))
can_catch = False   #중간에서 잡아줄 수 있는 상자가 있는지..

a = min(center)
b = max(center)
b_index = center.index(b)

for i in range(1, n):
    if ( center[i]>a and center[i]<b ) and (i > b_index):
        can_catch = True
        break

if (center[-1] - center[0] <= L) and can_catch:
    print("stable")
else:
    print("unstable")

"""
반례 
5 5
center = [0 5 4 -2 3]
-2와 3에서 안되는데 조건이 다 맞기 때문에 stable출력..

결국 하나씩 더해야한다는 결론..
"""

#틀림..

n, L = map(int, input().split())
center = list(map(int, input().split()))

if n <=2 :
    if max(center) - min(center) < L:
        print("stable")
    else:
        print("unstable")
else:#여기서 L과 같으면 안댐..
    if max(center) - min(center) <= L:
        print("stable")
    else:
        print("unstable")

"""
반례 
5 5
center = [0 5 0 5 0]
-2와 3에서 안되는데 조건이 다 맞기 때문에 stable출력..

결국 하나씩 더해야한다는 결론..
"""