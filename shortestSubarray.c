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
typedef struct {
    int idx,v;
} node;

node* stack;
int size;
int num;

void push(node a) 
{
    if(num==size)
    {
        size*=2;
        stack=realloc(stack,sizeof(node)*size);
    }
    stack[num++]=a;
}

node pop() 
{
    return stack[--num];
}

int bs(int a)
{
    int start=0;
    int end=num-1;
    int mid=0;
    while(start<=end)
    {
        mid=(start+end)/2;
        if(stack[mid].v>a)
            end=mid-1;
        else
            start=mid+1;
    }
    return start;
}

int shortestSubarray(int* A, int ASize, int K){
    size=2;
    stack=(node*)malloc(sizeof(node)*size);
    num=0;
    int* pre_sum=(int*)malloc(sizeof(int)*(ASize+1));
    memset(pre_sum,0,sizeof(int)*(ASize+1));
    int tmp=0;
    int i;
    for(i=0;i<ASize;i++)
    {
        tmp+=A[i];
        pre_sum[i+1]=tmp;
    }
    node n1;
    n1.v=0;
    n1.idx=0;
    push(n1);
    int out=12345678;
    for(i=1;i<ASize+1;i++)
    {
        int loc=bs(pre_sum[i]-K);
        if(loc>0)
        {
            out=min(out,i-stack[loc-1].idx);
        }
        while(num>0&&stack[num-1].v>=pre_sum[i])
        {
            pop();
        }
        n1.v=pre_sum[i];
        n1.idx=i;
        push(n1);
    }
    free(stack);
    free(pre_sum);
    return out==12345678? -1:out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int A[] = {84,-37,32,40,95};
    int K = 167;
    int len=sizeof(A)/sizeof(int);
    printf("%d\n",shortestSubarray(A,len,K));
#endif
    return 0;
}
    
