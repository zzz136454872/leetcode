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
int cmp(const void* a, const void* b)
{
    return *(int*)a-*(int*)b;
}

int* smallerNumbersThanCurrent(int* nums, int numsSize, int* returnSize){
    int* out=(int*)malloc(sizeof(int)*numsSize);
    int* tmp=(int*)malloc(sizeof(int)*numsSize);
    memcpy(tmp,nums,sizeof(int)*numsSize);
    qsort(tmp,numsSize,sizeof(int),cmp);
    int start,end,mid;
    for(int i=0;i<numsSize;i++)
    {
        start=0;
        end=numsSize-1;
        while(start<=end)
        {
            mid=(start+end)/2;
            if(tmp[mid]>=nums[i])
                end=mid-1;
            else
                start=mid+1;
        }
        out[i]=start;
    }
    free(tmp);
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
    int nums[] = {7,7,7,7};
    int returnSize;
    int numsSize=4;
    int* out=smallerNumbersThanCurrent(nums,numsSize,&returnSize);
    print_int_star(out,returnSize);
#endif
    return 0;
}
    
