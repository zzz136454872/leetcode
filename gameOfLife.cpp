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
public:
    void gameOfLife(vector<vector<int>>& board) {
        b=board;
        int c;
        cout<<"flag2"<<endl;
        for(int i=0;i<(int)board.size();i++)
        {
            for(int j=0;j<(int)board[0].size();j++)
            {
                cout<<"flag3"<<(int)board.size()<<(int)board[0].size()<<endl;
                c=count(i,j);
                if(b[i][j]==1)
                {
                    if(c<2||c>3)
                        board[i][j]=0;
                }
                else if(c==3)
                    board[i][j]=1;
            }
        }
    }

    int count(int i,int j)
    {
        int out=0;
        if(i>0)
            out+=b[i-1][j];
        if(j>0)
            out+=b[i][j-1];
        if(i>0&&j>0)
            out+=b[i-1][j-1];
        if(i<(int)b.size()-1)
            out+=b[i+1][j];
        if(j<(int)b[0].size()-1)
            out+=b[i][j+1];
        if(i<(int)b.size()-1&&j<(int)b[0].size()-1)
            out+=b[i+1][j+1];
        if(i>0&&j<(int)b[0].size()-1)
            out+=b[i-1][j+1];
        if(i<(int)b.size()-1&&j>0)
            out+=b[i+1][j-1];
        return out;
    }
        
private:
    vector<vector<int>> b;
};



#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;

    vector<vector<int>> in={
        {0,1,0},
        {0,0,1},
        {1,1,1},
        {0,0,0}
    };
    cout<<"flag1"<<endl;
    sl.gameOfLife(in);
    print(in);


    
#endif 
    return 0;
}

