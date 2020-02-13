#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int reverse(int x){
    int sign=1;
    int max=((unsigned int)(-1))>>1;
    int min=~max;
    if(x<=0)
    {
        if(x==0||x==min)
            return 0;
        sign=-1;
        x=-x;
    }

    char num[20]={0};
    int i=0;


    printf("%d, %d\n",max,min);

    while(x > 0)
    {
        //printf("%d\n",x);
        num[i++] = x % 10 + '0';
        x/=10;
    }
    //printf("%s\n",num);
    long long out1=0;
    for(i=0;i<strlen(num);i++)
        out1=out1*10+num[i]-'0';
    out1=sign*out1;
    if(out1>=min&&out1<=max)
        return (int)out1;
    else
        return 0;
}

int main()
{
    int a=-2147483648;
    int b=reverse(a);
    printf("%d\n",b);
    return 0;
}
