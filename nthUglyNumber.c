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
//丑数II
int nthUglyNumberII(int n){
    int table[1691];
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
    return table[n];
}

long long leastCommonMultiple(long long a, long long b)
{
    long long tmp,aa=a,bb=b;
    while(bb!=0)
    {
        tmp=bb;
        bb=aa%bb;
        aa=tmp;
    }
    return a*b/aa;
}

//丑数III
int nthUglyNumber(int n, int a, int b, int c){
    long long right=1000000000000000000+11;
    long long left=1;
    long long ab=leastCommonMultiple(a,b);
    long long ac=leastCommonMultiple(a,c);
    long long bc=leastCommonMultiple(b,c);
    long long abc=leastCommonMultiple(ab,c);
    long long mid;
    long long sum;
    while(left<right)
    {
        mid=(left+right)/2;
        sum=mid/a+mid/b+mid/c-mid/ab-mid/ac-mid/bc+mid/abc;
        if(sum<n)
            left=mid+1;
        else if(sum>n)
            right=mid-1;
        else
            right=mid;
    }
    return (int)left;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int n=4,a=2,b=3,c=4;
    int out=nthUglyNumber(n,a,b,c);
    printf("%d\n",out);
#endif
    return 0;
}
    
