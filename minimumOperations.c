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
// your code here
int minimumOperations(char* leaves){
    int n=strlen(leaves);
    int *r=(int*)malloc(sizeof(int)*n);
    int *ry=(int*)malloc(sizeof(int)*n);
    int *ryr=(int*)malloc(sizeof(int)*n);
    ry[0]=123456;
    ryr[0]=123456;
    if(leaves[0]=='y')
        r[0]=1;
    else
        r[0]=0;
    int out;
    for(int i=1;i<n;i++)
    {
        if(leaves[i]=='y')
        {
            r[i]=r[i-1]+1;
            ry[i]=min(r[i-1],ry[i-1]);
            ryr[i]=min(ry[i-1],ryr[i-1])+1;
        }
        else
        {
            r[i]=r[i-1];
            ry[i]=min(r[i-1],ry[i-1])+1;
            ryr[i]=min(ryr[i-1],ry[i-1]);
        }
    }
    out=ryr[n-1];
    //print_int_star(r,n);
    //print_int_star(ry,n);
    //print_int_star(ryr,n);
    free(r);
    free(ry);
    free(ryr);
    return out;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    //char *leaves = "rrryyyrryyyrr";
    char *leaves = "yry";
    printf("%d\n",minimumOperations(leaves));
#endif
    return 0;
}
    
