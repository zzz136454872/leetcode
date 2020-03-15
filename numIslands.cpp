/**
 * @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>
#include<queue>

using namespace std;

//显示中间结果
void print(vector<int> a)
{
    for(int i=0;i<(int)a.size();i++)
        cout<<a[i]<<" ";
    cout<<endl;
}

void print(vector<vector<int>> a)
{
    for(int i=0;i<(int)a.size();i++)
    {
        for(int j=0;j<(int)a[i].size();j++)
            cout<<a[i][j]<<" ";
        cout<<endl;
    }
}

void print(vector<bool> a)
{
    for(int i=0;i<(int)a.size();i++)
    {
        cout<<i<<" ";
        if(a[i])
            cout<<"true ";
        else
            cout<<"false ";
    }
    cout<<endl;
}

void print(bool a[],int len)
{
    for(int i=0;i<len;i++)
    {
        cout<<i<<" ";
        if(a[i])
            cout<<"true ";
        else
            cout<<"false ";
    }
    cout<<endl;
}

//#define testMod

#ifdef testMod
void test()
{
    
}
#endif

#ifndef testMod
class Solution {
private:
    vector<vector<char>> grid;
public:
    int numIslands(vector<vector<char>>& grid) {
        int count=0;
        this->grid=grid;
        for(int i=0;i<(int)grid.size();i++)
        {
            for(int j=0;j<(int)grid[0].size();j++)
            {
                if(this->grid[i][j]!='0')
                {
                    find(i,j);
                    count++;
                }
            }
        }
        return count;
    }

    int find(int i,int j)
    {
        if(i<0||j<0)
            return 0;
        if(i>=grid.size()||j>=grid[0].size())
            return 0;
        if(grid[i][j]=='0')
            return 0;
        grid[i][j]='0';
        find(i-1,j);
        find(i+1,j);
        find(i,j+1);
        find(i,j-1);
        return 0;
    }
};



#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<vector<char>> in=
    {11000,
        11000
        00100
        00011;
    cout<<sl.numIslands(in)<<endl;


    
#endif 
    return 0;
}

