bool isValid(char* s) {
    char stack[100000];
    int top=-1;
    for(int i=0;i<strlen(s);i++)
    {
        char c=s[i];
        if(c=='(' || c=='[' || c=='{')
        {
            stack[++top]=c;
        }
        else
        {
            if(top==-1)
            {
                return false;
            }
            char top1=stack[top--];
            if((c==')' && top1!='(') || (c==']' && top1!='[') || (c=='}' && top1!='{'))
            return false;
        }
    }

    return top==-1;
}