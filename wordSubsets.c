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

#ifndef testMod
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int check(char* word, int* table)
{
    int table2[26]={0};
    for(int i=0;i<strlen(word);i++)
        table2[word[i]-'a']++;
    for(int i=0;i<26;i++)
    {
        if(table2[i]<table[i])
            return 0;
    }
    return 1;
}

char ** wordSubsets(char ** A, int ASize, char ** B, int BSize, int* returnSize){
    int tableNow[26]={0},tableMax[26]={0};
    for(int i=0;i<BSize;i++)
    {
        memset(tableNow, 0, sizeof(int)*26);
        for(int j=0;j<strlen(B[i]);j++)
            tableNow[B[i][j]-'a']++;
        for(int j=0;j<26;j++)
            tableMax[j]=max(tableNow[j],tableMax[j]);
    }
    int bufferSize=100;
    char** out=(char**)malloc(sizeof(char**)*bufferSize);
    int count=0;
    for(int i=0;i<ASize;i++)
    {
        if(check(A[i],tableMax))
        {
            if(count==bufferSize)
            {
                bufferSize*=2;
                out=(char**)realloc(out,sizeof(char**)*bufferSize);
            }
            out[count++]=A[i];
        }
    }
    *returnSize=count;
    return out;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    char* A[] = {"amazon","apple","facebook","google","leetcode"};
    char* B[]={"e","o"};
    int aSize=5,bSize=2,returnSize;
    char** out=wordSubsets(A,aSize,B,bSize,&returnSize);
    printf("flag\n");
    print_char_2star(out,returnSize);
#endif
    return 0;
}
    
