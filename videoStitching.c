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

#ifndef testMod

#define min(a,b) (((a)<(b))?(a):(b))
int cmp(const void* a, const void* b)
{
    int **pa=(int**)a;
    int **pb=(int**)b;
    //printf("cmp: %d %d\n",**pa,**pb);
    if(**pa!=**pb)
        return **pa-**pb;
    return *(*pb+1)-*(*pa+1);
}

int videoStitching(int** clips, int clipsSize, int* clipsColSize, int T){
    qsort(clips,clipsSize,sizeof(int*),cmp);
    print_int_2star(clips,clipsSize,2);
    int log[101];
    int i;
    for(i=0;i<101;i++)
        log[i]=123456;
    log[0]=0;
    int *clip;
    int j;
    for(i=0;i<clipsSize;i++)
    {
        clip=clips[i];
        for(j=clip[0]+1;j<clip[1]+1;j++)
            log[j]=min(log[j],log[clip[0]]+1);
    }
    print_int_star(log,T+1);
    if(log[T]>1234)
        return -1;
    return log[T];
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int T = 10;
    
    int clipsSize=6;
    int**clips=(int**)malloc(sizeof(int*)*clipsSize);
    for(int i=0;i<clipsSize;i++)
        clips[i]=(int*)malloc(sizeof(int*)*2);
    int ori[6][2]={{0,2},{4,6},{8,10},{1,9},{1,5},{5,9}};
    for(int i=0;i<clipsSize;i++)
    {
        for(int j=0;j<2;j++)
            clips[i][j]=ori[i][j];
    }
    printf("%d\n",videoStitching(clips,clipsSize,NULL,T));
#endif
    return 0;
}
    
