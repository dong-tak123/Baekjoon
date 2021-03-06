# -*- coding: utf-8 -*-
"""약수의 개수와 덧셈

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aKGf_y3SGZHngXq7PNghkERkMUx58GBg

left부터 right까지의 수 중에서 약수의 갯수가 짝수면 더하고 홀수면 빼는 함수
"""

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        #약수의 갯수 구하기
        #약수의 갯수 초기화
        divider_count = 0
        for j in range(1, i//2 + 1):
            if (i % j == 0):
                divider_count += 1
        divider_count += 1
        
        if divider_count %2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer

#기댓값 43
print(solution(13,17))

