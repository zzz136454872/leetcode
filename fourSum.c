#include<stdio.h>
#include<stdlib.h>

int cmp(const void *pa,const void *pb)
{
    int a=*(int*)pa;
    int b=*(int*)pb;
    if(a > b)
        return 1;
    else if (a < b)
        return -1;
    return 0;
}
    
int** fourSum(int* nums, int numsSize, int target, int* returnSize, int** returnColumnSizes){
    int count=0;
    int size=100000;
    int i,j,k,l;
    qsort(nums,numsSize,sizeof(int),cmp);

    int (*ret)[4] = (int(*)[4])malloc(sizeof(int)*size*4);
    
    for(i=0;i<numsSize-3;i++)
    {
        for(j=i+1;j<numsSize-2;j++)
        {
            for(k=j+1;k<numsSize-1;k++)
            {
                for(l=k+1;l<numsSize;l++)
                {
                    //printf("%d, %d, %d, %d, %d\n",nums[i],nums[j],nums[k],nums[l],target);
                    if(nums[i]+nums[j]+nums[k]+nums[l]==target)
                    {
                        ret[count][0]=nums[i];
                        ret[count][1]=nums[j];
                        ret[count][2]=nums[k];
                        ret[count][3]=nums[l];
                        count++;
                    }
                }
            }
        }
    }

    //printf("%d\n",count);
                        
    int * rec=(int*)malloc(sizeof(int)*count);
    for(i=0;i<count+1;i++)
        rec[i]=4;
    *returnSize=count;
    return ret;
}

int main()
{
    const int size=6;
    int nums[6]  = {1, 0, -1, 0, -2, 2};
    int target=0;
    int (*out)[4];
    int ret_size;
    int *rec;
    out=fourSum(nums,size,target,&ret_size,&rec);

    int i;
    for(i=0;i<ret_size;i++)
        printf("%d, %d, %d, %d\n",out[i][0],out[i][1],out[i][2],out[i][3]);
    free(out);
    free(rec);
    return 0;
}
