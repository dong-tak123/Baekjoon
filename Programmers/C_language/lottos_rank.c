#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// lottos_len�� �迭 lottos�� �����Դϴ�.
// win_nums_len�� �迭 win_nums�� �����Դϴ�.
int* solution(int lottos[], size_t lottos_len, int win_nums[], size_t win_nums_len) {
    // return ���� malloc �� ���� �Ҵ��� ������ּ���. �Ҵ� ���̴� ��Ȳ�� �°� �������ּ���.
    int zero_count = 0;
    int same_num = 0;

    //0�� ������ �� ����
    for (int i = 0; i < lottos_len; i++) {
        if (lottos[i] == 0)
            zero_count++;
    }

    //���� ��� ������ ���� �ȴ�
    for (int i = 0; i < lottos_len; i++) {
        for (int j = 0; j < win_nums_len; j++) {
            if (lottos[i] == win_nums[j]) {
                same_num++;
                break;
            }
        }
    }
    //answer�� �޸𸮸� �������� �Ҵ��Ѵ�
    int* answer = (int*)malloc(sizeof(int) * 2);

    //����� Ȯ������
    answer[0] = 7 - same_num - zero_count;
    answer[1] = 7 - same_num;
    //����� 6�����ϱ� 7�̸� 1�� �ٲ�����..
    if (answer[0] == 7)
        answer[0] = 6;
    if (answer[1] == 7)
        answer[1] = 6;

    return answer;
}

int main(void) {
    //���⼭ �Է¹޴´�..
}