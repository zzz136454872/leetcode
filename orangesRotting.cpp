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

//#define testMod

#ifdef testMod
void test()
{
    vector<vector<int>> t1;
    vector<vector<int>> t2;
    vector<int> tmp;
    
    tmp.push_back(1);
    t1.push_back(tmp);
    t2=t1;
    t1.push_back(tmp);
    print(t1);
    cout<<"t2"<<endl;
    print(t2);
    
}
#endif


#ifndef testMod

class Solution {
private:
    vector<vector<int>> t1,t2;
public:
    int orangesRotting(vector<vector<int>>& grid) {
        t1=grid;
        t2=t1;
        if(t1.size()==0)
            return 0;
        if(t1[0].size()==0)
            return 0;
        int t=0;
        while(true)
        {
            if(finish())
                return t;
            if(t>100)
                break;
            for(int i=0;i<(int)grid.size();i++)
            {
                for(int j=0;j<(int)grid[0].size();j++)
                    t2[i][j]=rot(i,j);
            }
            t++;
            t1=t2;
        }

        return -1;
    }

    bool finish()
    {
        for(int i=0;i<(int)t1.size();i++)
        {
            for(int j=0;j<(int)t1[0].size();j++)
            {
                if(t1[i][j]==1)
                    return false;
            }
        }
        return true;
    }
    
    int rot(int i,int j)
    {
        if(t1[i][j]==1)
        {
            if(i>0&&t1[i-1][j]==2)
                return 2;
            if(j>0&&t1[i][j-1]==2)
                return 2;
            if(j<(int)t1[0].size()-1&&t1[i][j+1]==2)
                return 2;
            if(i<(int)t1.size()-1&&t1[i+1][j]==2)
                return 2;
            return 1;
        }
        return t1[i][j];
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
    vector<vector<int>> in = {{2,1,1},{1,1,0},{0,1,1}};
    int out = sl.orangesRotting(in);
    cout<<out<<endl;

    
#endif 
    return 0;
}


