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

void print(vector<string> a)
{
    for(int i=0;i<(int)a.size();i++)
        cout<<a[i]<<endl;
}

void print(vector<vector<string>> a)
{
    for(int i=0;i<(int)a.size();i++)
    {
        print(a[i]);
        cout<<endl;
    }
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
    int totalNQueens(int n) {
        
        string t(n,'.');
        for(int i=0;i<n;i++)
            tmp.push_back(t);
        this->n=n;
        out=0;
        add(0);
        return out;
    }

    void add(int row)
    {
        if(row==n)
        {
            out+=1;
            return;
        }
        for(int i=0;i<n;i++)
        {
            if(check(row,i))
            {
                tmp[row][i]='Q';
                add(row+1);
                tmp[row][i]='.';
            }
        }
    }

    bool check(int row, int column)
    {
        for(int i=0;i<n;i++)
        {
            if(tmp[row][i]=='Q'||tmp[i][column]=='Q')
                return false;
            if(row+i<n&&column+i<n&&tmp[row+i][column+i]=='Q')
                return false;
            if(row+i<n&&column-i>=0&&tmp[row+i][column-i]=='Q')
                return false;
            if(row-i>=0&&column+i<n&&tmp[row-i][column+i]=='Q')
                return false;
            if(row-i>=0&&column-i>=0&&tmp[row-i][column-i]=='Q')
                return false;
        }
        return true;
    }

private:
    int out;
    vector<string> tmp;
    int n;
};

#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    int out=sl.totalNQueens(10);
    cout<<out<<endl;
    
#endif 
    return 0;
}

