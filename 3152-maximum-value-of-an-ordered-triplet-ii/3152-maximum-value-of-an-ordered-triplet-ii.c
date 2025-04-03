long long maximumTripletValue(int* nums, int numsSize) {
    long max=0;
    long maxI=LLONG_MIN;

    long maxSuf[numsSize];
    maxSuf[numsSize-1]=nums[numsSize-1];
    for(int i=numsSize-2;i>=0;i--)
    {
        maxSuf[i]=(nums[i]>maxSuf[i+1])?nums[i]:maxSuf[i+1];
    }
    for(int j=1;j<numsSize-1;j++)
    {
        maxI=(nums[j-1]>maxI)?nums[j-1]:maxI;
        if(maxI!=LLONG_MIN && maxSuf[j+1]!=LLONG_MIN)
        {
            long cur=(maxI-nums[j])*maxSuf[j+1];
            if(cur>max)
            {
                max=cur;
            }
        }
    }
    return max;
}