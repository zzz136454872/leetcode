#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int myAtoi(char * str){

    int sign=1;
    int max=((unsigned int)(-1))>>1;
    int min=~max;
    int i=0;
    int len=strlen(str);

    while(i<len&&isspace(str[i]))
        i++;
    

    if(i==len)
        return 0;

    if(str[i]=='-')
    {
        sign=-1;
        i++;
    }
    else if(str[i] == '+')
        i++;
    else if(!isdigit(str[i]))
        return 0;

    //printf("flag1\n");
    
    long long out=0;
    
    for( ;isdigit(str[i]);i++)
    {
        out=out*10+str[i]-'0';
        if(out > max)
        {
            if(sign == 1)
                return max;
            else
                return min;
        }
    }
    return (int)out*sign;
}

int main()
{
    char a[]="-2147483648";
    int b=myAtoi(a);
    printf("%d\n",b);
    return 0;
}
