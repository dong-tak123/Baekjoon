#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//약수의 갯수를 구하자
int divider_count(int num) {
    int count = 0;
    //절반까지만 해서 거기에 자기자신은 항상 약수니까 +1을 해주면 된다
    for (int i = 1; i <= num / 2; i++) {
        if (num % i == 0)
            count++;
    }

    return (count + 1);
}

//약수의 홀짝에 따라 덧셈뺄셈을 정하자
int solution(int left, int right) {
    int answer = 0;

    for (int i = left; i < right + 1; i++) {
        if (divider_count(i) % 2 == 0)
            answer += i;
        else
            answer -= i;
    }

    return answer;
}

int main(void) {
    int result;

    result = solution(13, 17);
    printf("%d", result);
    //기댓값 43
}