#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// absolutes_len은 배열 absolutes의 길이입니다.
// signs_len은 배열 signs의 길이입니다.
int solution(int absolutes[], size_t absolutes_len, bool signs[], size_t signs_len) {
    int answer = 0;
    for (int i = 0; i < absolutes_len; i++)
    {
        if (signs[i])
            answer += absolutes[i];
        else
            answer -= absolutes[i];
    }
    return answer;
}

int main(void) {
    int a[5] = { 1,2,3,4,5 };
    bool s[5] = { true, false, true, false, true };
    int result;

    result = solution(a, 5, s, 5);
    printf("%d", result);
}