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
int minEatingSpeed(int* piles, int pilesSize, int h){
    int left=1;
    int right=1000000000;
    while(left<=right) {
        int mid=(left+right)/2;
        int tmp=0;
        for(int i=0;i<pilesSize;i++) {
            tmp+=(piles[i]+mid-1)/mid;
        }
        if(tmp>h)
            left=mid+1;
        else
            right=mid-1;
    }
    return left;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    // int piles[] = {3,6,7,11};
    int h = 8;

    // int piles[] = {30,11,23,4,20};
    h = 6;
    h = 5;
    int piles[] = {2,2};
    h=2;
    printf("%d\n",minEatingSpeed(piles,sizeof(piles)/sizeof(int),h));
#endif
    return 0;
}
    
