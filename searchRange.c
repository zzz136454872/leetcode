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
int* searchRange(int* nums, int numsSize, int target, int* returnSize){
    int* out=(int*)malloc(sizeof(int)*2);
    *returnSize=2;
    int start=0;
    int end=numsSize-1;
    int mid;
    while(start<=end)
    {
        mid=(start+end)/2;
        if(nums[mid]>=target)
            end=mid-1;
        else
            start=mid+1;
    }
    if(start<numsSize&&nums[start]==target)
        out[0]=start;
    else
        out[0]=-1;
    start=0;
    end=numsSize-1;
    while(start<=end)
    {
        mid=(start+end)/2;
        if(nums[mid]>target)
            end=mid-1;
        else
            start=mid+1;
    }
    if(end>=0&&nums[end]==target)
        out[1]=end;
    else
        out[1]=-1;
    return out;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int nums[]={5,7,7,8,8,10};
    //int numsSize=sizeof(nums)/sizeof(int);
    int numsSize=0;
    int outSize;
    int target=5;
    int* out=searchRange(nums,numsSize,target,&outSize);
    print_int_star(out,outSize);
#endif
    return 0;
}
    
