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
bool backspaceCompare(char * S, char * T){
    char s1[205]={0};
    char t1[205]={0};
    int p1=0,p2=0;
    for(int i=0;i<strlen(S);i++)
    {
        if(S[i]=='#')
        {
            if(p1>0)
                p1--;
        }
        else
            s1[p1++]=S[i];
    }
    for(int i=0;i<strlen(T);i++)
    {
        if(T[i]=='#')
        {
            if(p2>0)
                p2--;
        }
        else
            t1[p2++]=T[i];
    }
    if(p1!=p2)
        return false;
    for(int i=0;i<p1;i++)
    {
        if(s1[i]!=t1[i])
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
    char* S = "a##c";
    char* T = "#a#c";
    printf("%d\n",backspaceCompare(S,T));
#endif
    return 0;
}
    
