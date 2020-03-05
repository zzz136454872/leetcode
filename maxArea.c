#include<stdio.h>

#define min(a,b) ((a) > (b) ? (b):(a))

int maxArea(int* height, int heightSize){
    int i,j;
    int max=0,now=0;
    for(i=0;i<heightSize-1;i++)
    {
        for(j=i+1;j<heightSize;j++)
        {
            now=min(height[i],height[j])*(j-i);
            if(now > max)
            {
                max=now;
                //printf("%d, %d, %d\n",i,j,max);
            }
        }
        if(height[i] > height[i+1])
            i++;
    }
    return max;
}

int main()
{
    int test[]={1,8,6,2,5,4,8,3,7};
    int out=maxArea(test,9);
    
    printf("%d\n",out);
    return 0;
}
    
