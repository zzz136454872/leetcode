/* @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{
    cout<<"test"<<endl;
    if(string::npos==(long long)-1)
        cout<<"yes"<<endl;
    else
        cout<<"no"<<endl;
    cout<<(long long)string::npos<<endl;
    cout<<string::npos<<endl;
}
#endif

#ifndef testMod

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> out;
        if(words.size()==0)
        {
            return out;
        }

        int subLen=words[0].size();

        if(s.size()<words.size()*subLen)
            return out;

        int sum=0;
        
        for(unsigned long long i=0;i<words.size();i++)
            sum+=words[i][0];
            
        int *tmp = new int[words.size()];
        for(unsigned long long i=0;i<s.size()-subLen*words.size()+1;i++)
        {
            int tmpsum=0;
            for(unsigned long long j=i;j<i+subLen*words.size();j+=subLen) 
                tmpsum+=s[j];
            if(tmpsum!=sum)
                continue;
            
            for(unsigned long long j=0;j<words.size();j++)
                tmp[j]=0;
            bool may=true;
            for(unsigned long long j=i;j<i+subLen*words.size();j+=subLen)
            {
                bool find = false;
                for(unsigned long long k=0;k<words.size();k++)
                {
                    if(tmp[k])
                        continue;
                    if(s.find(words[k],j)==j)
                    {
                        find=true;
                        tmp[k]=1;
                        break;
                    }
                }
                if(!find)
                {
                    may=false;
                    break;
                }
            }
            if(!may)
            {
                continue;
            }
            //cout<<"Push"<<endl;
            out.push_back(i);
        }
        return out;
    }
    
private:

};


#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    string s = "barfoothefoobarman";
    vector<string> t = {"foo","bar"};
    vector<int> out=sl.findSubstring(s,t);
    for(unsigned long long i=0;i<out.size();i++)
        cout<<out[i]<<endl;

    
#endif 
    return 0;
}

