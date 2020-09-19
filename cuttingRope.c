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
    


