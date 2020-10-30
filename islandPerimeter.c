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
int islandPerimeter(int** grid, int gridSize, int* gridColSize){
    if(gridSize==0)
        return 0;
    int i,j;
    int y=gridSize,x=gridColSize[0];
    int out=0;
    for(i=0;i<y;i++)
    {
        for(j=0;j<x;j++)
        {
            if(grid[i][j])
            {
                if(i>0&&!grid[i-1][j])
                    out++;
                else if(i==0)
                    out++;
                if(j>0&&!grid[i][j-1])
                    out++;
                else if(j==0)
                    out++;
                if(i<y-1&&!grid[i+1][j])
                    out++;
                else if(i==y-1)
                    out++;
                if(j<x-1&&!grid[i][j+1])
                    out++;
                else if(j==x-1)
                    out++;
            }
        }
    }
    return out;
}
#endif

int main()
{
#ifdef testMod
    test();
#endif
#ifndef testMod
    const int gridSize=4;
    int *grid[gridSize];
    int grid1[]={0,1,0,0};
    int grid2[]={1,1,1,0};
    int grid3[]={0,1,0,0};
    int grid4[]={1,1,0,0};
    grid[0]=grid1;
    grid[1]=grid2;
    grid[2]=grid3;
    grid[3]=grid4;
    int gridColSize[]={4,4,4,4};

    printf("%d\n",islandPerimeter(grid,gridSize,gridColSize));

#endif
    return 0;
}
    
