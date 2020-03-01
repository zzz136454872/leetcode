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
    cout<<(-2)/3<<endl;
}
#endif

#ifndef testMod

class Solution {
public:
    int divide(int dividend, int divisor) {
        if(dividend==-2147483648&&divisor==-1)
            return 2147483647;
        long long  a=dividend;
        long long b=divisor;
        if(b == 1)
            return a;
        else if(b==-1)
            return -a;

        int sign=1;
        if(a==0)
            return 0;
        if(a < 0)
        {
            sign=-sign;
            a=-a;
        }
        if(b<0)
        {
            sign=-sign;
            b=-b;
        }
        int ans=0;
        fill(b);
        for(int i=30;i>=0;i--)
        {
            if(a+table[i]<0)
            {
                //cout<<"jmp"<<endl;
                continue;
            }
            //cout<<"i "<<i<<" table[i] "<<table[i]<<" a "<<a<<" count[i] "<<count[i]<<endl;
            a+=table[i];
            ans+=count[i];
        }
        if(sign == 1)
            return -ans;
        return ans;
    }

    void fill(int a)
    {
        if(a>0)
            a=-a;
        int i=0;
        table[0]=a;
        while(table[i] >= halfmax)
        {
            i++;
            table[i]=table[i-1]+table[i-1];
            //cout<<"i "<<i<<"table "<<table[i]<<" half "<<halfmax<<endl;
        }
        i++;
        for(;i<31;i++)
        {
            table[i] = -2147483649;
        }
        //for(i=0;i<31;i++)
        //    cout<<"i "<<i<<"table "<<table[i]<<" count "<<count[i]<<endl;
    }



private:
    int halfmax=-1073741824;
    long long table[32];
    long long count[32]={-1,-2,-4,-8,-16,-32,-64,-128,-256,-512,-1024,-2048,-4096,
                   -8192,-16384,-32768,-65536,-131072,-262144,-524288,
                   -1048576,-2097152,-4194304,-8388608,-16777216,-33554432,
                   -67108864,-134217728,-268435456,-536870912,-1073741824};
};

#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    cout<<sl.divide(-2147483648,-3)<<endl;
#endif 
    return 0;
}
