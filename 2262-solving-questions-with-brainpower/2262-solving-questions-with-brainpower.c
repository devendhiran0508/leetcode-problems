long long mostPoints(int** questions, int questionsSize, int* questionsColSize) {
    long n=questionsSize;
    long* a=(long*)calloc(n+1, sizeof(long));

    for(int i=n-1;i>=0;i--)
    {
        long skipq=questions[i][1];
        long next=i+skipq+1;

        long solve=questions[i][0];
        if(next<n)
        {
            solve+=a[next];
        }
        long skip=a[i+1];
        a[i]=(solve>skip)?solve:skip;
    }
    long res=a[0];
    return res;
}