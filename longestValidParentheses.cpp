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
#include<queue>

using namespace std;

//#define testMod

#ifdef testMod
class A 
{
    public:
        int getA()
        {
            return 1;
        } 
};

void test()
{
    queue<int> a;
    a.push(1);
    a.push(2);
    a.push(3);
    cout<<a.front()<<endl;
    cout<<a.back()<<endl;
    a.pop();
    cout<<a.front()<<endl;
    cout<<a.size()<<endl;
    cout<<endl<<endl;

    A aa;
    A *pa=&aa;
    cout<<pa->getA()<<endl;
}
#endif

#ifndef testMod
typedef struct {
    int start;
    int end;
} cut;

class Solution {
public:
    int longestValidParentheses(string s) {
        queue<cut> t1;
        cut c;
        
        ////cout<<"start"<<endl;

        for(long long i=0;i<(long long)s.size()-1;i++)
        {
            if(s[i]=='('&&s[i+1]==')')
            {
                c.start=i;
                c.end=i+1;
                //print(c);
                t1.push(c);
            }
        }

        ////cout<<"start1"<<endl;
        queue<cut> t2;
        queue<cut> *from,*to;
        bool change=false;
        cut c2;
        while(true)
        {
            //cout<<"round"<<endl;
            if(t1.size()==0)
            {
                from=&t2;
                to=&t1;
            }
            else 
            {
                from=&t1;
                to=&t2;
            }
            change=false;
            while(from->size() > 0)
            {
                //cout<<"inside"<<endl;
                c=from->front();
                from->pop();
                if(c.start>0 && c.end<(int)s.size()-1&&
                   s[c.start-1]=='('&&s[c.end+1]==')')
                {
                    c.start--;
                    c.end++;
                    to->push(c);
                    //print(c);
                    change=true;
                    continue;
                }
                if(from->size()==0)
                {
                    to->push(c);
                    break;
                }
                c2=from->front();
                //print(c2);
                if(c2.start==c.end+1)
                {
                    //cout<<"now"<<endl;
                    c.end=c2.end;
                    from->pop();
                    change=true;
                }
                to->push(c);
                //cout<<to->size()<<endl;
            }
            if(!change)
                break;
        }

        int max=0;
        //cout<<"end size "<<to->size()<<endl;
        while(to->size() > 0)
        {
            c=to->front();
            to->pop();
            if(max < c.end-c.start+1)
                max=c.end-c.start+1;
        }
        return max;
    }
private:
    void print(cut& a)
    {
        cout<<"start "<<a.start<<" end "<<a.end<<endl;
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
    string in="()(())";
    int out=sl.longestValidParentheses(in);
    cout<<out<<endl;
#endif 
    return 0;
}

