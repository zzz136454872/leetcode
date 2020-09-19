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

bool isUgly(int num){
    if(num==0)
        return false;
    while(num%2==0)
        num>>=1;
    while(num%3==0)
        num/=3;
    while(num%5==0)
        num/=5;
    return num==1;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod

#endif
    return 0;
}
    
