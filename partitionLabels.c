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
typedef struct s{
    int start;
    int end;
} node;
    
int* partitionLabels(char * S, int* returnSize){
    int bufferSize=2;
    int *buffer=malloc(sizeof(int)*bufferSize);
    int i; 
    int count=0;
    node log[26];
    for(i=0;i<26;i++) {
        log[i].start=-1;
        log[i].end=-1;
    }
    int c;
    
    for(i=0;i<strlen(S);i++) {
        c=S[i]-'a';
        if(log[c].start==-1)
            log[c].start=i;
        log[c].end=i;
    }

    i=0;
    int nowEnd=0;
    int preEnd=-1;
    while(i<strlen(S)) {
        if(i>nowEnd) {
            if(count==bufferSize) {
                bufferSize*=2;
                buffer=(int*)realloc(buffer,sizeof(int)*bufferSize);
            }
            buffer[count]=nowEnd-preEnd;
            preEnd=nowEnd;
            count++;
            nowEnd=i;
        }
        while(i<=nowEnd) {
            nowEnd=max(nowEnd,log[S[i]-'a'].end);
            i++;
        }
    }
    if(count==bufferSize) {
        bufferSize*=2;
        buffer=(int*)realloc(buffer,sizeof(int)*bufferSize);
    }
    buffer[count]=nowEnd-preEnd;
    count++;
    *returnSize=count;
    return buffer;
}

#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    printf("running\n");
    char* S = "ababcbacadefegdehijhklij";
    int returnSize;
    int* out=partitionLabels(S, &returnSize);
    print_int_star(out,returnSize);
#endif
    return 0;
}
    

