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
char findTheDifference(char * s, char * t){
    int i;
    int len1=strlen(s);
    int len2=strlen(t);
    int log[26]={0};
    for(i=0;i<len2;i++)
        log[t[i]-'a']++;
    for(i=0;i<len1;i++)
        log[s[i]-'a']--;
    for(i=0;i<26;i++)
    {
        if(log[i])
            return (char)(i+'a');
    }
    return 'a'; //error
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    char s[] = "";
    char t[] = "a";
    printf("%c\n", findTheDifference(s,t));
#endif
    return 0;
}
    
