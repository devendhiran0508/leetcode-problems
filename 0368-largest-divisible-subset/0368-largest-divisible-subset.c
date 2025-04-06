/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

int* largestDivisibleSubset(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    int* dp = (int*)malloc(numsSize * sizeof(int));
    int* prev = (int*)malloc(numsSize * sizeof(int)); 
    int maxSize = 1, maxIndex = 0;

    qsort(nums, numsSize, sizeof(int), compare); 

    for (int i = 0; i < numsSize; i++) {
        dp[i] = 1;
        prev[i] = -1;
        for (int j = 0; j < i; j++) {
            if (nums[i] % nums[j] == 0 && dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1;
                prev[i] = j;
            }
        }
        if (dp[i] > maxSize) {
            maxSize = dp[i];
            maxIndex = i;
        }
    }

    int* result = (int*)malloc(maxSize * sizeof(int));
    *returnSize = maxSize;
    int index = maxSize - 1;

    while (maxIndex != -1) {
        result[index--] = nums[maxIndex];
        maxIndex = prev[maxIndex];
    }

    free(dp);
    free(prev);

    return result;
}