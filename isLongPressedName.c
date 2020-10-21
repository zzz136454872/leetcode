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
bool isLongPressedName(char * name, char * typed){
    int i=0;
    char log1[1001],log2[1001];
    int count1[1001]={0},count2[1001]={0};
    int p1=-1,p2=-1;
    for(i=0;i<strlen(name);i++)
    {
        if(i==0||name[i]!=name[i-1])
        {
            p1++;
            log1[p1]=name[i];
            count1[p1]=1;
        }
        else
            count1[p1]++;
    }
    for(i=0;i<strlen(typed);i++)
    {
        if(i==0||typed[i]!=typed[i-1])
        {
            p2++;
            log2[p2]=typed[i];
            count2[p2]=1;
        }
        else
            count2[p2]++;
    }
    if(p1!=p2)
        return false;
    for(i=0;i<p1+1;i++)
    {
        if(log1[i]!=log2[i])
            return false;
        if(count1[i]>count2[i])
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
    char* name="alex";
    char*  typed = "aaleex";
    printf("%d\n",isLongPressedName(name, typed));
#endif
    return 0;
}
    
