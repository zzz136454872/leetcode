#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

//#define testMod

#ifdef testMod
void test()
{
    vector<string> ss;
    string test="test";
    ss.push_back(test);
    test="test1";
    ss.push_back(test);
    cout<<"in test"<<endl;
    for(unsigned long long i=0;i<ss.size();i++)
        cout<<ss[i]<<endl;
    cout<<ss.size()<<endl;
}
#endif

class Solution {
public:    
    vector<string> letterCombinations(string digits) {
        vector<string> out;
        return out;
    }

private:
    
};

int main()
{
#ifdef testMod
    test();
#endif
    Solution sl;


    return 0;
}
