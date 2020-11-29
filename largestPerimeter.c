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
int cmp(const void* pa, const void *pb)
{
    return *(int*)pb-*(int*)pa;
}
int largestPerimeter(int* A, int ASize){
    int i;
    qsort(A,ASize,sizeof(int),cmp);
    for(i=0;i<ASize-2;i++)
    {
        if(A[i]<A[i+1]+A[i+2])
            return A[i]+A[i+1]+A[i+2];
    }
    return 0;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int A[]={3,6,2,3};
    int length=sizeof(A)/sizeof(int);
    int out=largestPerimeter(A,length);
    printf("%d\n",out);
#endif
    return 0;
}
    
