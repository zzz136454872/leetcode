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
//剪绳子
int cuttingRope0(int n){
    if(n<=4)
    {
        switch(n)
        {
            case 2:
                return 1;
            case 3:
                return 2;
            case 4:
                return 4;
            default:
                return -1;
        }
    }
    int base=1;
    for(int i=0;i<n/3;i++)
        base*=3;
    switch(n%3)
    {
        case 0:
            return base;
        case 1:
            return 4*base/3;
        default:
            return 2*base;
    }
}

//剪绳子II
int cuttingRope(int n){
    if(n<=4)
    {
        switch(n)
        {
            case 2:
                return 1;
            case 3:
                return 2;
            case 4:
                return 4;
            default:
                return -1;
        }
    }
    long long base=1;
    for(int i=0;i<n/3-1;i++)
        base=(3*base)%1000000007;
    switch(n%3)
    {
        case 0:
            return (3*base)%1000000007;
        case 1:
            return (4*base)%1000000007;
        case 2:
            return (6*base)%1000000007;
        default:
            printf("error in switch\n");
            exit(-1);
    }
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int num=10;
    printf("%d\n",cuttingRope(num));
#endif
    return 0;
}
    


