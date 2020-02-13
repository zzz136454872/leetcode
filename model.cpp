#include<iostream>
using namespace std;

class Solution {
public:
    string intToRoman(int num) {
        
        string roman[] = {"M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"};
        int nums[] =     {1000,900, 500, 400,100,  90, 50,  40, 10,   9,  5,   4,  1};
        int i=0;
        string out="";
        while(num > 0)
        {
            if(num>=nums[i])
            {
                num -= nums[i];
                out+=roman[i];
            }
            else
                i++;
        }
        return out;
    }
};

int main()
{
    Solution sl;
    int in = 58;
    cout<<"flag1"<<endl;
    string out = sl.intToRoman(in);
    cout<<out<<endl;
    return 0;
}


