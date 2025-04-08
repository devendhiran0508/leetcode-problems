bool hasDuplicates(int* nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] == nums[j]) {
                return true;
            }
        }
    }
    return false;
}


int minimumOperations(int* nums, int numsSize) {
     int operations = 0;

    while (numsSize > 0 && hasDuplicates(nums, numsSize)) {
        if (numsSize <= 3) {
            numsSize = 0; // Remove all remaining elements if fewer than 3
        } else {
            for (int i = 0; i < numsSize - 3; i++) {
                nums[i] = nums[i + 3]; // Shift elements left by 3
            }
            numsSize -= 3;
        }
        operations++;
    }

    return operations;

}