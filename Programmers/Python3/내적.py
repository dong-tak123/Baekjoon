# -*- coding: utf-8 -*-
"""내적

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v_bDhaEctqYB7eOnPpBR6bL36j1PjidF
"""

def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        answer += a[i]*b[i]

    return answer