#include<stdio.h>
#include<malloc.h>
#include<string.h>

char * longestPalindrome(char * s) 
{
    int loc=0;
    int len =strlen(s);
    int max=0;
    int start,end;
    char *out = (char*)malloc(sizeof(char)*len+1);
    out[0]=0;
    for(loc=0;loc<len;loc++)
    {
        start=loc;
        end=loc;
        while(start>=0&&end<len&&s[start]==s[end])
        {
            start--;
            end++;
        }
        if(max<end-start-1)
        {
            max = end - start-1;
            strncpy(out,s+start+1,max);
            out[max]=0;
        }
        if(loc < len-1 && s[loc] == s[loc+1])
        {
            start=loc;
            end = loc + 1;
            while(start>=0&&end<len&&s[start]==s[end])
            {
                start--;
                end++;
            }
            if(max < end - start -1)
            {
                max = end - start-1;
                strncpy(out,s+start+1,max);
                out[max]=0;
            }
        }
    }
    return out;
}
        
int main()
{
    //char test[]="ababa";
    char test[]="";
    char *out=longestPalindrome(test);
    printf("%s\n",out);
    free(out);
    return 0;
}
