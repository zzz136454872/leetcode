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
int gcd(int a,int b)
{
    if(b==0)
        return a;
    return gcd(b,a%b);
}

bool isGoodArray(int* nums, int numsSize){
    int g=nums[0];
    for(int i=1;i<numsSize;i++)
        g=gcd(g,nums[i]);
    return g==1;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int nums[] = {12,4};
    int len=sizeof(nums)/sizeof(int);
    printf("%d\n",isGoodArray(nums,len));
#endif
    return 0;
}
    
