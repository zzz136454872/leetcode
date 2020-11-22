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
bool isAnagram(char * s, char * t){
    int log[128]={0};
    int i;
    for(i=0;i<strlen(s);i++)
        log[s[i]]++;
    for(i=0;i<strlen(t);i++)
        log[t[i]]--;
    for(i=0;i<128;i++)
    {
        if(log[i])
            return false;
    }
    return true;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    char* s = "rat";
    char* t = "car";
    printf("%d\n",isAnagram(s,t));
#endif
    return 0;
}
    
