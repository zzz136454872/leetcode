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
int findKthNumber(int m, int n, int k){
    int left=1,right=30000*30000;
    while(left<=right) {
        int mid=(left+right)/2;
        int tmp=0;
        for(int i=1;i<=n;i++) {
            tmp+=min(mid/i,m);
            if(mid<=i)
                break;
        }
        if(tmp>=k)
            right=mid-1; 
        else
            left=mid+1;
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
    int m = 3, n = 3, k = 5;
    m = 2, n = 3, k = 6;
    printf("%d\n",findKthNumber(m,n,k));
#endif
    return 0;
}
    
