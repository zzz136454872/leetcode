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
    vector<vector<string>> s;
    vector<string> tmp;
    tmp.push_back("test");
    s.push_back(tmp);
    tmp.pop_back();
    tmp.push_back("test1");
    s.push_back(tmp);
    vector<vector<string>> another;
    another=s;
    another.pop_back(); 
    for(unsigned long long i=0;i<s.size();i++)
        for(unsigned long long j=0;j<s[i].size();j++)
            cout<<i<<" "<<j<<" "<<s[i][j]<<endl;
    for(unsigned long long i=0;i<another.size();i++)
        for(unsigned long long j=0;j<another[i].size();j++)
            cout<<i<<" "<<j<<" "<<another[i][j]<<endl;
    
}
#endif

#ifndef testMod

typedef struct {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
}ListNode ;

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<ListNode*> log = lists;
        ListNode* out,*end;
        bool allnull=true;
        for(unsigned long long i=0;i<lists.size();i++)
        {
            if(lists[i]!=NULL)
            {
                allnull=false;
                break;
            }
        }
        if(allnull)
            return NULL;
        int min=999999999;
        int minloc=-1;
        for(unsigned long long i=0;i<log.size();i++)
        {
            if(log[i]==NULL)
                continue;
            if(log[i]->val<min)
            {
                min=log[i]->val;
                minloc=i;
            }
        }
        end=log[minloc];
        out=log[minloc];
        log[minloc]=log[minloc]->next;
        
        while(true)
        {
            allnull=true;
            min=999999999;
            minloc=-1;
            for(unsigned long long i=0;i<log.size();i++)
            {
                if(log[i]==NULL)
                    continue;
                allnull=false;
                if(log[i]->val<min)
                {
                    min=log[i]->val;
                    minloc=i;
                }
            }
            if(allnull)
                break;
            end->next=log[minloc];
            end=end->next;
            log[minloc]=log[minloc]->next;
        }
        return out;
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

#endif 
    return 0;
}

