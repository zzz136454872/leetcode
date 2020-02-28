
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

typedef struct {
    int val;
    ListNode *next;
    //ListNode(int x) : val(x), next(NULL) {}
}ListNode ;

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *end=NULL,*out=NULL;
        
        ListNode *tmp1=l1,*tmp2=l2;
        if(l1==NULL)
            return l2;
        else if(l2==NULL)
            return l1;
        if(tmp1->val< tmp2->val)
        {
            end=tmp1;
            out=tmp1;
            tmp1=tmp1->next;
        }
        else
        {
            end=tmp2;
            out=tmp2;
            tmp2=tmp2->next;
        }
        while(tmp1!=NULL&&tmp2!=NULL)
        {
            if(tmp1->val < tmp2->val)
            {
                end->next=tmp1;
                end=end->next;
                tmp1=tmp1->next;
            }
            else
            {
                end->next=tmp2;
                end=end->next;
                tmp2=tmp2->next;
            }
        }
        if(tmp1!=NULL)
            end->next=tmp1;
        else
            end->next=tmp2;

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

