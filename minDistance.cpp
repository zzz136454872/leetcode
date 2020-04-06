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

void print(vector<vector<int> > a)
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
#define min(a,b) ((a)<(b)?(a):(b))
class Solution {
public:
    int minDistance(string word1, string word2) {
        this->s1=word1;
        this->s2=word2;
        size1=(int)s1.size();
        size2=(int)s2.size();
        log=new int[size1*size2];
        for(int i=0;i<size1*size2;i++)
            log[i]=-1;
        int out= minDis(0,0);
        delete [] log;
        return out;
    }

    int minDis(int loc1,int loc2)
    {
        if(loc1==size1)
        {
            return size2-loc2;
        }
        else if(loc2==size2)
        {
            return size1-loc1;
        }
        int tmp=read(loc1,loc2);
        if(tmp!=-1)
        {
            return tmp;
        }
        int t1=minDis(loc1+1,loc2+1);
        int t2=minDis(loc1,loc2+1);
        int t3=minDis(loc1+1,loc2);
        if(!(s1[loc1]==s2[loc2]))
        {
            tmp=min(min(t1,t2),t3)+1;
        }
        else
        {
            tmp=min(min(t1,t2+1),t3+1);
        }
        write(loc1,loc2,tmp);
        return tmp;
    }

    int read(int loc1,int loc2)
    {
        return log[loc1*size2+loc2];
    }

    void write(int loc1,int loc2,int value)
    {
        log[loc1*size2+loc2]=value;
    }
        
private:
    string s1,s2;
    int size1,size2;
    int *log;
};

#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    string s1="rse";
    string s2="s";

    int out=sl.minDistance(s1,s2);
    cout<<out<<endl;
#endif 
    return 0;
}


