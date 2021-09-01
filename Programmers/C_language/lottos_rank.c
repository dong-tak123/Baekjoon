#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// lottos_len은 배열 lottos의 길이입니다.
// win_nums_len은 배열 win_nums의 길이입니다.
int* solution(int lottos[], size_t lottos_len, int win_nums[], size_t win_nums_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int zero_count = 0;
    int same_num = 0;

    //0의 갯수를 다 세자
    for (int i = 0; i < lottos_len; i++) {
        if (lottos[i] == 0)
            zero_count++;
    }

    //현재 몇개가 같은지 보면 된다
    for (int i = 0; i < lottos_len; i++) {
        for (int j = 0; j < win_nums_len; j++) {
            if (lottos[i] == win_nums[j]) {
                same_num++;
                break;
            }
        }
    }
    //answer에 메모리를 동적으로 할당한다
    int* answer = (int*)malloc(sizeof(int) * 2);

    //등수를 확인하자
    answer[0] = 7 - same_num - zero_count;
    answer[1] = 7 - same_num;
    //등수가 6까지니까 7이면 1로 바꿔주자..
    if (answer[0] == 7)
        answer[0] = 6;
    if (answer[1] == 7)
        answer[1] = 6;

    return answer;
}

int main(void) {
    //여기서 입력받는다..
}