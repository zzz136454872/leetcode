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
        vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
            start=beginWord;
            stop=endWord;
            string now=start;
            vector<bool> log(wordList.size(),false);
            this->list=wordList;
            return findpath(now);
        }

        vector<vector<string>> findpath(string now,vector<bool> log) {
            cout<<now<<endl;
            vector<string> tmp;
            vector<vector<string>> out;
            string t=now;
            if(now.compare(stop)==0)
            {
                tmp.push_back(stop);
                out.push_back(tmp);
                return out;
            }
            for(int i=0;i<(int)list.size();i++)
            {
                if(log[i]==false&&diff(now,list[i])==1)
                {
                    log[i]=true;
                    if(index!=list.end())
                    {
                        vector<vector<string>> l_out=findpath(log[i]);
                        for(auto vs:l_out)
                        {
                            vs.insert(vs.begin(),now);
                            out.insert(out.begin(),vs);
                        }
                    }
                }
            }
            return out;
        }

        int diff(string a,string b)
        {
            int out=0;
            for(int i=0;i<(int)a.size();i++)
            {
                if(a[i]!=b[i])
                    out++;
            }
            return out;
        }

    private:
        string start,stop;
        vector<string> list;
};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    vector<string> wordList={"hot","dot","dog","lot","log","cog"};
    string beginWord = "hit",endWord = "cog";
    vector<vector<string>> out=sl.findLadders(beginWord,endWord,wordList);
    for(auto vs:out)
    {
        for(string a:vs)
            cout<<a<<" ";
        cout<<endl;
    }
#endif 
    return 0;
}

