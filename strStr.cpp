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
        list[')']=')';
        list['(']=0;
        list['[']=0;
        list['{']=0;
    }
    
    bool isValid(string s) {
        
        return 

    }
private:
    map<char,char> list;
    return 

};
#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    string haystack = "abababc",needle = "ababc";
    int test=sl.strStr(haystack,needle);
    cout<<"test: "<<test<<endl;

#endif 
    return 0;
}

