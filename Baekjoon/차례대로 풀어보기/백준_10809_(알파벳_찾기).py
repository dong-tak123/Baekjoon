# -*- coding: utf-8 -*-
"""백준 10809 (알파벳 찾기)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15G0BEzPut54_Ol2Q-nVc9w-LhkfLD60m

**문제**

- 알파벳이 단어에서 언제 제일 처음 나오는지 구하라

**키 포인트**

- ord()를 이용해서 아스키 코드값으로 바꿀 수 있다..
"""

#ord()를 생각하지 못했을 때..

S = input()
check = {'a' : -1,'b' : -1,'c' : -1,'d' : -1,'e' : -1,'f' : -1,'g' : -1,
         'h' : -1,'i' : -1,'j' : -1,'k' : -1,'l' : -1,'m' : -1,'n' : -1,
         'o' : -1,'p' : -1,'q' : -1,'r' : -1,'s' : -1,'t' : -1,'u' : -1,
         'v' : -1,'w' : -1,'x' : -1,'y' : -1,'z' : -1,}

for i in range(len(S)):
    if check[S[i]] == -1:
        check[S[i]] = i

for value in check.values():
    print(value, end = " ")

#ord()를 알고난 후..

S = input()

check = [-1] * 26

for i in range(len(S)):
    if check[ord(S[i])-97] == -1:
        check[ord(S[i])-97] = i

for num in check:
    print(num, end=" ")

