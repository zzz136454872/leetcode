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

void print(vector<vector<char>> a)
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
    void solve(vector<vector<char>>& board) {
        int count=0;
        this->grid=board;
        for(int i=0;i<(int)grid.size();i++)
        {
            for(int j=0;j<(int)grid[0].size();j++)
            {
                if(this->grid[i][j]=='O')
                {
                    if(!find(i,j))
                        fill(i,j);
                    count++;
                }
            }
        }
        for(int i=0;i<(int)grid.size();i++)
        {
            for(int j=0;j<(int)grid[0].size();j++)
            {
                if(this->grid[i][j]=='X')
                {
                    board[i][j]='X';
                }
                else
                    board[i][j]='O';
            }
        }
    }

    int find(int i,int j)
    {
        if(i<0||j<0)
            return 1;
        if(i>=grid.size()||j>=grid[0].size())
            return 1;
        if(grid[i][j]!='O')
            return 0;
        cout<<"i "<<i<<" j "<<j<<endl;
        grid[i][j]='1';
        print(grid);
        cout<<endl;
        return find(i-1,j)+
        find(i+1,j)+
        find(i,j+1)+
        find(i,j-1);
    }

    void fill(int i,int j)
    {
        if(i<0||j<0)
            return;
        if(i>=grid.size()||j>=grid[0].size())
            return;
        if(grid[i][j]=='X')
            return;
        grid[i][j]='X';
        fill(i-1,j);
        fill(i+1,j);
        fill(i,j+1);
        fill(i,j-1);
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
    {{'X','X','X','X'},
        {'X','O','O','X'},
        {'X','X','O','X'},
        {'X','O','X','X'}};
    print(in);
    sl.solve(in);
    print(in);

#endif 
    return 0;
}

