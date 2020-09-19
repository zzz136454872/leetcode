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
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        log=vector<vector<int>>(obstacleGrid.size(),vector<int>(obstacleGrid[0].size(),-1));
        return findPath(0,0,obstacleGrid);
    }

    int findPath(int x,int y,vector<vector<int>> &grid)
    {
        if(x>=(int)grid.size()||y>=(int)grid[0].size())
            return 0;
        if(grid[x][y]==1)
            return 0;
        if(x==(int)grid.size()-1&&y==(int)grid[0].size()-1)
            return 1;
        if(log[x][y]!=-1)
            return log[x][y];
        log[x][y]=findPath(x,y+1,grid)+findPath(x+1,y,grid);
        return log[x][y];
    }
        
private:
    vector<vector<int>> log;
};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<vector<int>> grid={{0,0,0}, {0,1,0}, {0,0,0}};
    cout<<sl.uniquePathsWithObstacles(grid)<<endl;
#endif 
    return 0;
}

