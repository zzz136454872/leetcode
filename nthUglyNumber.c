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
int nthUglyNumber(int n){
    int* table=(int*)malloc(sizeof(int)*(n+1));
    table[0]=0;
    table[1]=1;
    int a=1,b=1,c=1;
    for(int i=2;i<n+1;i++)
    {
        table[i]=min(table[a]*2,table[b]*3);
        table[i]=min(table[i],table[c]*5);
        if(table[i]==table[a]*2)
            a++;
        if(table[i]==table[b]*3)
            b++;
        if(table[i]==table[c]*5)
            c++;
    }
    int out=table[n];
    free(table);
    return out;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod

#endif
    return 0;
}
    
