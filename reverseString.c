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
// your code here
void reverseString(char* s, int sSize){
    char tmp;
    int i=0;
    int j=sSize-1;
    while(i<j)
    {
        tmp=s[i];
        s[i]=s[j];
        s[j]=tmp;
        i++;
        j--;
    }
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    char s[]="hello";
    reverseString(s,strlen(s));
    printf("%s\n", s);
#endif
    return 0;
}
    
