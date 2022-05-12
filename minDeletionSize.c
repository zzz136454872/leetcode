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
int minDeletionSize(char ** strs, int strsSize){
    int n=strlen(strs[0]);
    int i,j;
    int res=0;
    int prev=-1;
    for(i=0;i<n;i++) {
        prev=-1;
        for(j=0;j<strsSize;j++) {
            if(strs[j][i]<prev) {
                // printf("%d %d %d %d\n",i,j,strs[j][i],prev);
                res++;
                break;
            } else {
                prev=strs[j][i];
            }
        }
    }
    return res;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    int nStr=3;
    char** strs = (char**)malloc(nStr*sizeof(char*));
    char s[][5] = {"rrjk","furt","guzm"};
    int i;
    for(i=0;i<nStr;i++) {
        strs[i]=(char*)malloc((strlen(s[i])+1)*sizeof(char));
        strcpy(strs[i],s[i]);
    }
    printf("%d\n",minDeletionSize(strs,nStr));
#endif
    return 0;
}
    
