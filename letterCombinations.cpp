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
    {
        for(unsigned long long j=0;j<ss[i].size();j++)
        {

            cout<<ss[i][j]<<endl;
        }
    }
    cout<<ss.size()<<endl;
}
#endif

#ifndef testMod
class Solution
{
private:
    vector<string> out;
    string nums;
    string num[10] = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};

public:    
    vector<string> letterCombinations(string digits) {
        if(digits.size()==0)
            return out;
        nums=digits;
        getstring(0,"");
        return out;
    }

    void getstring(unsigned long long loc,string str)
    {
        //cout<<loc<<" "<<nums<<" "<<str<<endl;
        if(loc==nums.size())
        {
            out.push_back(str);
            return ;
        }
        //cout<<num[nums[loc]-'0']<<endl;
        for(unsigned long long i=0;i<num[nums[loc]-'0'].size();i++)
        {
            //cout<<i<<endl;
            getstring(loc+1,str+num[nums[loc]-'0'][i]);
        }
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
    string a ="23";
    vector<string> out = sl.letterCombinations(a);
    cout<<"main"<<endl;
    for(unsigned long long i=0;i<out.size();i++)
        cout<<out[i]<<endl;
    
#endif
    return 0;
}
