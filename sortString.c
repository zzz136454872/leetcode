/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include"ctools.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

//#define testMod
#ifdef testMod
void test() 
{

}
#endif

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

#ifndef testMod
char* sortString(char * s){
    int i;
    int len=strlen(s);
    char* ss=(char*)malloc(len+1);
    memset(ss,0,len+1);
    int count2=0;
    int min_loc,min_val;
    int max_loc,max_val;
    int pre_min,pre_max;
    while(count2<len)
    {
        pre_min=0;
        while(true)
        {
            min_loc=-1;
            min_val=127;
            for(i=0;i<len;i++)
            {
                if(s[i]!='0'&&s[i]<min_val&&s[i]>pre_min)
                {
                    min_loc=i;
                    min_val=s[i];
                }
            }
            if(min_loc==-1)
                break;
            ss[count2++]=min_val;
            s[min_loc]='0';
            pre_min=min_val;
            //printf("%s, %s ,%c \n",s,ss,pre_min);
        }
        //printf("flag\n");
        pre_max=127;
        while(true)
        {
            max_loc=-1;
            max_val=0;
            for(i=0;i<len;i++)
            {
                if(s[i]!='0'&&s[i]>max_val&&s[i]<pre_max)
                {
                    max_loc=i;
                    max_val=s[i];
                }
            }
            if(max_loc==-1)
                break;
            ss[count2++]=max_val;
            s[max_loc]='0';
            pre_max=max_val;
            //printf("%s, %s ,%c \n",s,ss,pre_min);
        }
    }
    memcpy(s,ss,len);
    free(ss);
    return s;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    char s[]= "leetcode";
    //char s[]= "aaaabbbbcccc";
    char* out=sortString(s);
    printf("%s\n",out);
#endif
    return 0;
}
    
