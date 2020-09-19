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
int nthSuperUglyNumber(int n, int* primes, int primesSize){
    int table[100001];
    table[0]=0;
    table[1]=1;
    int index[100];
    for(int i=0;i<100;i++)
        index[i]=1;
    int tmp;
    for(int i=2;i<=n;i++)
    {
        tmp=2147483647;
        for(int j=0;j<primesSize;j++)
            tmp=min(tmp,primes[j]*table[index[j]]);
        table[i]=tmp;
        for(int j=0;j<primesSize;j++)
        {
            if(primes[j]*table[index[j]]==tmp)
                index[j]++;
        }
    }
    print_int_star(table,n+1);
    return table[n];
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
   int n=12;
   int primes[]={2,7,13,19} ;
   printf("%d\n",nthSuperUglyNumber(n,primes,4));
#endif
    return 0;
}
    
