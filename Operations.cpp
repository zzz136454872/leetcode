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

class Operations {
public:
    Operations() {

    }

    int minus(int a, int b) {
        return a+(-b);
    }

    int multiply(int a, int b) {
        int sign=1;
        if(a==0||b==0)
            return 0;
        if(a==1)
            return b;
        if(b==1)
            return a;
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
        fill(a);
        for(int i=30;i>=0;i--)
        {
            if(b+count[i]<0)
            {

                //cout<<"b "<<b<<" i "<<i<<" count "<<count[i]<<endl;
                continue;
            }
            //cout<<"i "<<i<<" table[i] "<<table[i]<<" b "<<b<<" count[i] "<<count[i]<<" ans "<<ans<<endl;
            b+=count[i];
            ans+=table[i];
        }
        if(sign==1)
            return -ans;
        return ans;
    }

    int divide(int a, int b) {
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
                continue;
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
            table[i] = -2147483648;
        }
        //for(i=0;i<31;i++)
        //    cout<<"i "<<i<<"table "<<table[i]<<" count "<<count[i]<<endl;
    }



private:
    int halfmax=-1073741824;
    int table[32];
    int count[32]={-1,-2,-4,-8,-16,-32,-64,-128,-256,-512,-1024,-2048,-4096,
                   -8192,-16384,-32768,-65536,-131072,-262144,-524288,
                   -1048576,-2097152,-4194304,-8388608,-16777216,-33554432,
                   -67108864,-134217728,-268435456,-536870912,-1073741824};
};

/**
 * Your Operations object will be instantiated and called as such:
 * Operations* obj = new Operations();
 * int param_1 = obj->minus(a,b);
 * int param_2 = obj->multiply(a,b);
 * int param_3 = obj->divide(a,b);
 */

#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Operations op;
    cout<<op.multiply(-13969484,-5)<<endl;
#endif 
    return 0;
}
