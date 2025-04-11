int countSymmetricIntegers(int low, int high) {
    int count=0;
    for(int i=low;i<=high;i++)
    {
        int n=i;
        int digit=0,temp=n;

        while(temp>0)
        {
            digit++;
            temp/=10;
        }
        if(digit%2!=0)
            continue;
        int half=digit/2;
        int sum1=0,sum2=0;
        temp=n;
        for(int j=0;j<digit;j++)
        {
            int dig=temp%10;
            if(j<half)
            {
                sum2+=dig;
            }
            else
            {
                sum1+=dig;
            }
            temp/=10;
        }
        if(sum1==sum2)
        {
            count++;
        }

    }
    return count;
}