/* @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{
    cout<<"test"<<endl;
    vector<int> out;
    out.push_back(100);
    cout<<out[0]<<endl;
}
#endif

#ifndef testMod

int count(vector<int> &a)
{
    unsigned long long num=0;
    while(num<a.size())
    {
        if(!a[num])
            return num;
        else num++;
    }
    return num;
}

typedef struct 
{
    int index;
    int count;
} row;

bool cmp(row a, row b)
{
    if(a.count < b.count)
        return true;
    else if(a.count==b.count && a.index<b.index)
        return true;
    return false;
} 

class Solution {
private:


public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        row *tmp=new row[mat.size()];
        for(unsigned long long i=0;i<mat.size();i++)
        {
            tmp[i].index=i;
            tmp[i].count=count(mat[i]);
        }
        for(int i=0;i<mat.size();i++)
            cout<<tmp[i].count<<" "<<tmp[i].index<<endl;
        sort(tmp,tmp+mat.size(),cmp);
        cout<<endl;
        vector<int> out;

        for(int i=0;i<mat.size();i++)
            cout<<tmp[i].count<<" "<<tmp[i].index<<endl;
        for(int i=0;i<k;i++)
        {
            out.push_back(tmp[i].index);
        }
        return out;
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
    cout<<"main"<<endl;
    vector<vector<int>> mat = {{1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0},{1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0},{1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0},{1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0},{1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0},{1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0},{1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1},{1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0},{1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0},{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0},{1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0},{1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0}};
    int k = 7;
    vector<int> out=sl.kWeakestRows(mat,k);
    for(unsigned long long i=0;i<(unsigned long long)k;i++)
        cout<<out[i]<<endl;
#endif 
    return 0;
}

