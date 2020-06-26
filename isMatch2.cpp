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

void print(bool a)
{
    if(a)
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
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
    bool isMatch(string s, string p) {
        this->s=s;
        //this->p=shorten(p);
        this->p=p;
        cout<<"shorten p "<<this->p<<endl;
        for(int i=(int)(this->p).size(),j=(int)s.size();i>0&&j>0;i--,j--)
        {
            if((this->p)[i]=='*')
                break;
            if(!match(s[j],(this->p)[i]))
                return false;
        }
        log = new int[s.size()*(this->p.size())];
        for(int i=0;i<(int)(s.size()*(this->p.size()));i++)
            log[i]=0;
        return test(0,0);
    }

    string shorten(string p)
    {
        int start=-1,end=-1;
        for(int i=0;i<(int)p.size();i++)
        {
            if(p[i]=='*')
            {
                if(start==-1)
                    start=i;
                end=i;
            }
        }
        cout<<"start "<<start<<" end "<<end<<endl;
        if(start<end)
            return p.substr(start)+p.substr(end);
        else
            return p;
    }

    bool match(char a, char b)
    {
        //cout<<"match "<<a<<" "<<b<<endl;
        if(a == b)
            return true;
        return b=='?';
    }

    bool test(int s_loc,int p_loc)
    {
        if(log[s_loc*s.size()+p_loc]==-1)
            return false;
        else if(log[s_loc*s.size()+p_loc]==1)
            return true;
        cout<<"test "<<s_loc<<" "<<p_loc<<endl;
        while(s_loc<(int)s.size()&&p_loc<(int)p.size()&&match(s[s_loc],p[p_loc]))
        {
            //cout<<s[s_loc]<<p[p_loc]<<endl;
            s_loc++;
            p_loc++;
        }
        //if(s_loc > 10 || p_loc>10)
        //  exit(0);
        cout<<"test1 "<<s_loc<<" "<<p_loc<<endl;
        if(s_loc==(int)s.size())
        {
            if(p_loc==(int)p.size())
            {
                log[s_loc*s.size()+p_loc]=1;
                return true;
            }
            for(int i=p_loc;i<(int)p.size();i++)
            {
                if(p[i]!='*')
                {
                    log[s_loc*s.size()+i]=-1;
                    return false;
                }
            }
            log[s_loc*s.size()+p_loc]=1;
            return true;
        }
        if(p[p_loc]=='*')
        {
            if(test(s_loc,p_loc+1))
            {
                log[s_loc*s.size()+p_loc]=1;
                return true;
            }
            cout<<"flag0 "<<s_loc<<" "<<p_loc<<endl;
            while(s_loc<(int)s.size())
            {
                if(test(s_loc+1,p_loc+1))
                {
                    return true;
                }
                cout<<"flag "<<s_loc<<" "<<p_loc<<endl;
                s_loc++;
            }
            log[s_loc*s.size()+p_loc]=-1;
            return false;
        }
        log[s_loc*s.size()+p_loc]=-1;
        return false;
    }
private:
    string s,p;
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
    string s="aa";
    string p="a*";
    if(sl.isMatch(s,p))
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;
#endif 
    return 0;
}
