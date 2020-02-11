/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include<stdio.h>
#include<stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
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

int main()
{
    const int size=4;
    int nums[4]={1,3,100,-1};
    int target=101;
    int *out;
    int ret_size;
    out=twoSum(nums,size,target,&ret_size);
    int i;
    printf("now\n");
    for(i=0;i<ret_size;i++)
        printf("%d, ",out[i]);
    free(out);
    return 0;
}
