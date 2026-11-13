#include <stdlib.h>

long long countNonDecreasingSubarrays(int* nums, int numsSize, int k) {
    int* values = (int*)malloc(numsSize * sizeof(int));
    int* counts = (int*)malloc(numsSize * sizeof(int));

    if(values == NULL || counts == NULL) {
        free(values);
        free(counts);
        return 0;
    }

    int front = 0, back = -1;
    int right = numsSize - 1;

    long long ans = 0;
    long long cost = 0;

    for(int left = numsSize - 1; left >= 0; left--) {
        int cnt = 1;

        while(front <= back && values[back] < nums[left]) {
            cost += 1LL * (nums[left] - values[back]) * counts[back];

            cnt += counts[back];
            back--;
        }

        back++;
        values[back] = nums[left];
        counts[back] = cnt;

        while(cost > k) {
            cost -= values[front] - nums[right];

            if(counts[front] == 1) {
                front++;
            }
            else {
                counts[front]--;
            }

            right--;
        }

        ans += right - left + 1LL;
    }

    free(values);
    free(counts);

    return ans;
}