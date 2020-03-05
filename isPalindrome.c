#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

bool isPalindrome(int x){
    if(x < 0)
        return false;
    if(x == 0)
        return true;
    char tmp[20]={0};
    int i=0;
    while
    {
        tmp[i++]=x % 10 + '0';
        x/=10;
    }
    i--;
    int j=0;
    while(tmp[i]==tmp[j])
    {
        i--;
        j++;
        if(i >= j)
            return true;
    }
    return false;
}

int main()
{
    char a[]="1234321";
    int b=isPalindrome(a);
    printf("%d\n",b);
    return 0;
}
