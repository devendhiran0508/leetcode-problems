bool canJump(int* nums, int numsSize) {
    int max=0;
    for(int i=0;i<numsSize;i++)
    {
        if(i>max)
            return false;
        max=(i+nums[i]>max)?i+nums[i]:max;
        if(max>=numsSize-1)
        {
            return true;
        }
    }
    return true;
}