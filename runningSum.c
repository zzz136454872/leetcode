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
int* runningSum(int* nums, int numsSize, int* returnSize){
    int* out=(int*)malloc(sizeof(int)*numsSize);
    memset(out,0,sizeof(int)*numsSize);
    out[0]=nums[0];
    for(int i=1;i<numsSize;i++)
        out[i]=nums[i]+out[i-1];
    *returnSize=numsSize;
    return out;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int inp[]={3,1,2,10,1};
    int outSize;
    int* out=runningSum(inp,sizeof(inp)/sizeof(int),&outSize);
    print_int_star(out,outSize);
#endif
    return 0;
}
    
