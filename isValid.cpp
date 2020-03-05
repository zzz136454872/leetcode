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
    
}
#endif

#ifndef testMod

class Solution {
public:
    Solution() {
        list['}']='{';
        list[']']='[';
        list[')']='(';
    }
    
    bool isValid(string s) {
        char tmp;
        for(unsigned long long i=0;i<s.size();i++)
        {
            if(s[i] == '('|| s[i]=='{'||s[i]=='[')
                st.push(s[i]);
            else
            {
                if(st.empty())
                {
                    return false;
                }
                else
                {
                    tmp=st.top();
                    if(tmp!=list[s[i]])
                    {
                        cout<<"flag"<<endl;
                        return false;
                    }
                    st.pop();
                }
            }
        }
        return st.empty();
    }
private:
    map<char,char> list;
    stack<char> st;

};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    string in="()";
    bool test=sl.isValid(in);
    if(test)
        cout<<"true"<<endl;
    else
        cout<<"false"<<endl;

#endif 
    return 0;
}

