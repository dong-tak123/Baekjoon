#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// a_len은 배열 a의 길이입니다.
// b_len은 배열 b의 길이입니다.
int solution(int a[], size_t a_len, int b[], size_t b_len) {
    int answer = 0;

    for (int i = 0; i < a_len; i++)
    {
        answer += a[i] * b[i];
    }
    return answer;
}

int main(void) {
    int a[5] = { 1,2,3,4,5 };
    int b[5] = { 1,2,3,4,5 };
    int result;

    result = solution(a, 5, b, 5);
    printf("%d", result);
}