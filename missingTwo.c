/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void print_int_star(int *list, int len)
{
    for(int i=0;i<len;i++)
        printf("%d ",list[i]);
    putchar('\n');
}

void print_int_2star(int **matrix,int row,int col)
{
    for(int i=0;i<row;i++)
        print_int_star(matrix[i],col);
}

#define max(a,b) (((a)>(b))?(a):(b))

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* missingTwo(int* nums, int numsSize, int* returnSize){
    int* out=(int*)malloc(2*sizeof(int));
    *returnSize=2;
    long long suma2b2=0;
    long long sumab=0;
    for(int i=1;i<numsSize+3;i++)
    {
        suma2b2+=i*i;
        sumab+=i;
    }
    for(int i=0;i<numsSize;i++)
    {
        suma2b2-=nums[i]*nums[i];
        sumab-=nums[i];
    }

    int ab=(sumab*sumab-suma2b2)/2;
    sumab=-sumab;
    
    for(int i=1;i<numsSize+3;i++)
    {
        if(i*i+sumab*i+ab==0)
        {
            out[0]=i;
            out[1]=-sumab-i;
            return out;
        }
    }
    return NULL;
}

int main()
{
    int nums[]={1};
    int outSize;
    int *out=missingTwo(nums,1,&outSize);
    print_int_star(out,outSize);
    free(out);
    return 0;
}
    
