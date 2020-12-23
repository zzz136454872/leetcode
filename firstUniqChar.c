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
int firstUniqChar(char * s){
    long long count[26]={0};
    int n=strlen(s);
    for(int i=0;i<strlen(s);i++)
        count[s[i]-'a']+=n+i;
    long long minNum=123456789;
    for(int i=0;i<26;i++)
    {
        if(count[i]>0)
            minNum=min(minNum, count[i]);
    }
    if(minNum<2*n)
        return minNum-n;
    return -1;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    char *s= "loveleetcode";
    printf("%d\n",firstUniqChar(s));
#endif
    return 0;
}
    
