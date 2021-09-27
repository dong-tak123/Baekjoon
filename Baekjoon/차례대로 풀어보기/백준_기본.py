# -*- coding: utf-8 -*-
"""백준 기본

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ScYhHQapBqOJkds3qeYS1iLOeIlo4ayz
"""

a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

a,b,c = map(int, input().split())

print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

a = int(input())
b = int(input())
sum=a*b
while (b>0):
    print(a*(b%10))
    b = b//10
print(sum)

print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")

print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')

"""if문"""

a,b = map(int, input().split())

if a<b:
    print("<")
elif a==b:
    print("==")
else:
    print(">")

score = int(input())

if score>=90 :
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")

year = int(input())

if (((year%4 == 0) and (year%100 != 0)) or (year%400 == 0)):
    print("1")
else:
    print("0")

x = int(input())
y = int(input())

if x*y>0:
    if x>0:
        print("1")
    else:
        print("3")
else:
    if x>0:
        print("4")
    else:
        print("2")

h, m = map(int, input().split())

if m>=45:
    print(h, m-45)
else:
    if h==0:
        print(23, m+15)
    else:
        print(h-1, m+15)

"""for"""

N = int(input())

for i in range(1,10):
    print(f"{N} * {i} = {N*i}")

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    print(a+b)

n = int(input())
print(n*(n+1)//2)

n = int(input())

for i in range(1,n+1):
    print(i)

n = int(input())

for i in range(1,n+1):
    print(n-i+1)

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a+b}")

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {a} + {b} = {a+b}")

"""while문"""

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break

"""문자열"""

letter = input()
print(ord(letter))

T = int(input())

for _ in range(T):
    r, s = input().split()
    r = int(r)
    for i in s:
        print(i*r, end="")
    print()

a, b = map(str, input().split())

a, b = int(a[::-1]), int(b[::-1])
if a>b:
    print(a)
else:
    print(b)

dial={"A":3,"D":4,"G":5,"J":6,"M":7,"P":8,"S":8,"V":9,"Y":10,
      "B":3,"E":4,"H":5,"K":6,"N":7,"Q":8,"T":9,"W":10,"Z":10,
      "C":3,"F":4,"I":5,"L":6,"O":7,"R":8,"U":9,"X":10}
    
letter = input()
sum=0
for i in letter:
    sum += dial[i]
print(sum)

"""기본수학 1"""

#2839
N = int(input())
box = 0

#남은 설탕이 5의 배수가 될때까지 3을 뺀다..
while N>=0:
    if N%5 == 0:
        box += N//5
        break
    N -= 3
    box += 1
if N%5 != 0:
    print(-1)
else:
    print(box)

"""기본수학 2"""

point_x = {}
point_y = {}

for i in range(1, 4):
    a, b = map(int, input().split())
    if a in point_x:
        point_x[a] += 1
    else:
        point_x[a] = 1
    if b in point_y:
        point_y[b] += 1
    else:
        point_y[b] = 1

for i in point_x:
    if point_x[i] == 1:
        print(i, end=" ")
        break
for i in point_y:
    if point_y[i] == 1:
        print(i, end=" ")
        break

#4153

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    else:
        nums.sort()
        if nums[0]**2 + nums[1]**2 == nums[2]**2:
            print("right")
        else:
            print("wrong")

