#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int cmp(const void *pa, const void *pb)
{
    char a=*(char*)pa;
    char b=*(char*)pb;
    return a-b;
}


int countCharacters(char ** words, int wordsSize, char * chars){
    int i;
    char used[100]={0};
    int j;
    int out=0;
    int p1;
    int len=strlen(chars);
    for(i=0;i<wordsSize;i++)
    {
        p1=0;
        j=0;
        for(j=0;j<100;j++)
            used[j]=0;
        printf("flag2:i: %d\n",i);
        printf("len: %d\n",(int)strlen(words[i]));

        while(p1<strlen(words[i]))
        {
            printf("flag3\n");
            for(j=0;j<len;j++)
            {
                if(chars[j]==words[i][p1]&&used[j]==0)
                {
                    used[j]=1;
                    break;
                }
            }
            if(j==len)
                break;
            p1++;
        }

        if(p1==strlen(words[i]))
        {
            printf("%s\n",words[i]);
            out+=p1;
        }
    }
    return out;
}

int main()
{
    char *in[]={"hello","world","leetcode"};
    char chars[] = "welldonehoneyr";
    printf("flag1\n");
    int out=countCharacters((char**)in,4,chars);
    printf("%d\n",out);
    return 0;
}
    
