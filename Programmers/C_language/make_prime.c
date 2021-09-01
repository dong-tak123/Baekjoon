#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int IsPrime(int n) {
    for (int i = 2; i < n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

// nums_len�� �迭 nums�� �����Դϴ�.
int solution(int nums[], size_t nums_len) {
    int answer = 0;
    int i, j, k;
    int sum;

    //3���� �����ϵ��� for���� ������..
    for (i = 0; i < nums_len - 2; i++) {
        for (j = i + 1; j < nums_len - 1; j++) {
            for (k = j + 1; k < nums_len; k++) {
                sum = nums[i] + nums[j] + nums[k];
                if (IsPrime(sum))
                    answer++;
            }
        }
    }

    return answer;
}

int main(void) {
    int arr[5] = { 1,2,7,6,4 };
    int result;

    result = solution(arr, 5);
    printf("%d", result);
}