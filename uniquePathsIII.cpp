/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */
#include"cpptools.h"
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod
class Solution {
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        for(int i=0;i<(int)grid.size();i++)
        {
            for(int j=0;j<(int)grid[0].size();j++)
                if(grid[i][j]==1)
                    return findPath(i,j,grid);
        }
        return -1; // will not go to here
    }

    int findPath(int x,int y,vector<vector<int>>& grid)
    {
        if(x<0||x>=(int)grid.size()||y<0||y>=(int)grid[0].size())
            return 0;
        if(grid[x][y]==-1)
            return 0;
        if(grid[x][y]==2)
        {
            if(check(grid))
                return 1;
            return 0;
        }
        grid[x][y]=-1;
        int out=findPath(x+1,y,grid)+findPath(x-1,y,grid)+
            findPath(x,y+1,grid)+findPath(x,y-1,grid);
        grid[x][y]=0;
        return out;
    }
    
    bool check(vector<vector<int>>& grid)
    {
        for(int i=0;i<(int)grid.size();i++)
        {
            for(int j=0;j<(int)grid[0].size();j++)
            {
                if(grid[i][j]==0)
                    return false;
            }
        }
        return true;
    }
            
private:
};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<vector<int>> grid={{1,0,0,0},{0,0,0,0},{0,0,2,-1}};
    cout<<sl.uniquePathsIII(grid)<<endl;
#endif 
    return 0;
}

