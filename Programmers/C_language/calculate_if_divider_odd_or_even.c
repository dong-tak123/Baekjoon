#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//����� ������ ������
int divider_count(int num) {
    int count = 0;
    //���ݱ����� �ؼ� �ű⿡ �ڱ��ڽ��� �׻� ����ϱ� +1�� ���ָ� �ȴ�
    for (int i = 1; i <= num / 2; i++) {
        if (num % i == 0)
            count++;
    }

    return (count + 1);
}

//����� Ȧ¦�� ���� ���������� ������
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
    //��� 43
}