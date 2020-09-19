#ifndef cpptools_h
#define cpptools_h
#include<iostream>
#include<string>
#include<vector>

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
#endif
