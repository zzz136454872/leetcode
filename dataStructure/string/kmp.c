#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int* getNext(char *str)
{
    int len=strlen(str);
    int* next=(int*)malloc(len);
    next[0]=-1;
    int i=0;
    int k=-1;
    while(i<len-1)
    {
        if(k==-1||str[i]==str[k])
        {
            i++;
            k++;
            next[i]=k;
        }
        else
            k=next[k];
    }
    return next;
}

int kmpMatch(char* a, char *b)
{
    int i=0;
    int j=0;
    int lenA=strlen(a);
    int lenB=strlen(b);
    int* next=getNext(b);
    while(i<lenA&&j<lenB)
    {
        if(j==-1||a[i]==b[j])
        {
            i++;
            j++;
        }
        else
            j=next[j];
    }
    free(next);
    if(j==lenB)
        return i-lenB;
    return -1;
}

int main()
{
    char *a="abcaab";
    char *b="aaaaaa";
    printf("%d\n",kmpMatch(a,b));
    return 0;
}
