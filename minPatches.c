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
int minPatches(int* nums, int numsSize, int n){
    int i=0;
    long long x=1;
    int out=0;
    while(x<=n)
    {
        if(i<numsSize&&nums[i]<=x)
            x+=(long long)nums[i++];
        else
        {
            x*=2;
            out++;
        }
    }
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int nums[]={1,5,10};
    int n = 20;
    int len=sizeof(nums)/sizeof(int);
    printf("%d\n",minPatches(nums,len,n));
#endif
    return 0;
}
    
