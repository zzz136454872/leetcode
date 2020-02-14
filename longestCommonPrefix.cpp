#include<iostream>
#include<string>
#include<vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size()==0)
            return "";
        string out;
        int cut;
        int high,low=0;
        high=strs[0].size();
        bool all=true;
        while(low<high)
        {
            cut=(low+high+1)/2;
            out=strs[0].substr(0,cut);
            all=true;
            for(unsigned long long i = 1; i < strs.size();i++)
            {
                cout<<out<<" "<<i<<" "<<strs[i]<<" "<<strs[i].find(out)<<endl;
                if(strs[i].find(out)!=0)
                {
                    high=cut-1;
                    cout<<endl;
                    all=false;
                    break;
                }
            }
            if(!all)
                continue;
            low=cut;
        }
        out=strs[0].substr(0,low);
        return out;
    }
};

int main()
{
    Solution sl;
    string test="flight";
    vector<string> strs;
    strs.push_back("a");
    //strs.push_back("flow");
    //strs.push_back(test);
    string out=sl.longestCommonPrefix(strs);
    cout<<out<<endl;
    return 0;
}


