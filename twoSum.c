/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include<stdio.h>
#include<stdlib.h>
#include"ctools.h"

int* twoSum0(int* nums, int numsSize, int target, int* returnSize){
    int i;
    int j;
    int *out = (int*)malloc(2*sizeof(int));
    for(i=0;i<numsSize-1;i++)
        for(j=i+1;j<numsSize;j++)
        {
            if(nums[i]+nums[j]==target)
            {
                out[0]=i;
                out[1]=j;
                *returnSize=2;
            }
        }
    return out;
}

typedef struct {
    int val;
    int loc;
}pair;

int cmp(const void *a, const void* b)
{
    return ((pair*)a)->val-((pair*)b)->val;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    pair* table=(pair*)malloc(sizeof(pair)* numsSize);
    int i;
    for(i=0;i<numsSize;i++)
    {
        table[i].val=nums[i];
        table[i].loc=i;
    }
    qsort(table,numsSize, sizeof(pair),cmp);
    *returnSize=2;
    int j=numsSize-1;
    i=0;
    int *out=(int*)malloc(sizeof(int)*2);
    int tmp;
    while(i<j)
    {
        tmp=table[i].val+table[j].val;
        if(tmp==target)
        {
            out[0]=table[i].loc;
            out[1]=table[j].loc;
            break;
        }
        else if(tmp>target)
            j--;
        else
            i++;
    }
    free(table);
    return out;
}

int main()
{
    const int size=4;
    int nums[4]={1,3,100,-1};
    int target=101;
    int ret_size;
    int* out=twoSum(nums,size,target,&ret_size);
    print_int_star(out, ret_size);
    free(out);
    return 0;
}
