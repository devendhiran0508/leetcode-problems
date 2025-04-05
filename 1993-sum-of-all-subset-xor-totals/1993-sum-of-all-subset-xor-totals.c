int subsetXORSum(int* nums, int numsSize) {
    int res=0;
    int total=1<<numsSize;

    for(int i=0;i<total;i++)
    {
        int sum=0;
        for(int j=0;j<numsSize;j++)
        {
            if(i & (1<<j))
            {
                sum ^=nums[j];
            }
        }
        res+=sum;
    }
    return res;
}