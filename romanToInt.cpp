#include<iostream>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        string roman[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int nums[] =     {1000,900, 500, 400,100,  90, 50,  40, 10,   9,  5,   4,  1};
        int i=0;
        int out=0;
        string str = s;
        
        //int round=0;
        
        while(s.size() > 0)
        {
            //cout<<s<<endl;
            //cout<<nums[i]<<endl;
            //round++;
            //if(round>20)
             //   exit(0);
            if(s.find(roman[i])==0)
            {
                s=s.substr(roman[i].size());
                out+=nums[i];
            }
            else
            {
                i++;
            }
        }
        return out;
    }
    
};

int main()
{
    Solution sl;
    string  s = "LVIII";

    int out = sl.romanToInt(s);
    cout<<out<<endl;
    return 0;
}

