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

int cmpByStart(const void* a, const void* b) {
    return (*(int**)a)[0]-(*(int**)b)[0];
}

int cmpByIdx(const void* a, const void* b) {
    return (*(int**)a)[2]-(*(int**)b)[2];
}

int* findRightInterval(int** intervals, int intervalsSize, int* intervalsColSize, int* returnSize){
    int** i3=(int**)malloc(sizeof(int*)*intervalsSize);
    int i;
    for(i=0;i<intervalsSize;i++) {
        i3[i]=(int*)malloc(sizeof(int)*4);
        i3[i][0]=intervals[i][0];
        i3[i][1]=intervals[i][1];
        i3[i][2]=i;
    }
    qsort(i3,intervalsSize,sizeof(int*),cmpByStart);
    int left,right,mid;
    for(i=0;i<intervalsSize;i++) {
        left=i;
        right=intervalsSize-1;
        while(left<=right) {
            mid=(left+right)/2;
            if(i3[mid][0]>=i3[i][1])
                right=mid-1;
            else
                left=mid+1;
        }
        if(left==intervalsSize)
            i3[i][3]=-1;
        else
            i3[i][3]=i3[left][2];
    }
    qsort(i3,intervalsSize,sizeof(int*),cmpByIdx);
    int* res=(int*)malloc(sizeof(int)*intervalsSize);
    for(i=0;i<intervalsSize;i++) {
        res[i]=i3[i][3];
        free(i3[i]);
    }
    free(i3);
    *returnSize=intervalsSize;
    return res;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    // int intervals[][2] = {{1,2}};
    // int intervals[][2] = {{3,4},{2,3},{1,2}};
    int intervals[][2] = {{1,4},{2,3},{3,4}};
    int resSize;
    int** i2=malloc_int_2star((int*)intervals,3,2);
    int* ii=findRightInterval(i2,3,NULL,&resSize);
    print_int_star(ii,resSize);
#endif
    return 0;
}
    
