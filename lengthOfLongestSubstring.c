#include<stdio.h>
#include<string.h>

int lengthOfLongestSubstring(char* s){
    int count[129]={0};
    int max=0;
    int start=0,end=0;
    while(end < strlen(s))
    {
        printf("out1: %c,%c\n",s[start],s[end]);
        if(count[s[end]])
        {
            if(end-start> max)
                max=end-start;
            while(s[start] != s[end])
            {
                printf("%c, %c\n",s[start],s[end]);
                count[s[start]]=0;
                start++;
            }
            start++;
        }
        else
        {
            count[s[end]]=1;
        }
        printf("out2: %c,%c\n",s[start],s[end]);
        end++;
        printf("%d,%d,%d\n",end,start,max);
    }
    printf("%d,%d,%d\n",end,start,max);
    if(max < end - start)
        max=end-start;
    return max;
}

int main()
{
    //char in[] = "abcabcbb";
    char in[] = "test";
    int a = lengthOfLongestSubstring(in);
    printf("%d\n",a);
    return 0;
}
    
    
