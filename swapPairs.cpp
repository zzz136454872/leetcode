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

struct ListNode {
    int val;
    ListNode *next;
};

ListNode* getnode(int x)
{
    ListNode *t=new ListNode;
    t->next=NULL;
    t->val=x;
    return t;
}

class Solution {
private:


public:
    ListNode* swapPairs(ListNode* head) {
        if(head==NULL||head->next==NULL)
            return head;
        ListNode *tmp0=NULL,*tmp1=head,*tmp2=head->next,*tmp3=tmp2->next;
        tmp1->next=tmp3;
        tmp2->next=tmp1;
        head=tmp2;
        show(head);
        while(true)
        {
            cout<<"tmp1 "<<tmp1->val<<endl;
            cout<<"tmp2 "<<tmp2->val<<endl;
            tmp0=tmp1;
            tmp1=tmp0->next;
            if(tmp1==NULL)
            {
                cout<<"end1"<<endl;
                return head;
            }
            tmp2=tmp1->next;
            if(tmp2==NULL)
            {
                cout<<"end2"<<endl;
                return head;
            }
            tmp3=tmp2->next;
            if(tmp3==NULL)
                cout<<"tmp3 null"<<endl;
            else
                cout<<"tmp3 "<<tmp3->val<<endl;
            tmp1->next=tmp3;
            tmp2->next=tmp1;
            tmp0->next=tmp2;
        }
    }

    void show(ListNode* head)
    {
        cout<<"show"<<endl;
        while(head!=NULL)
        {
            cout<<head->val<<" ";
            head=head->next;
        }
        cout<<endl;
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
    ListNode* head=getnode(1), *end=head;
    for(int i=0;i<3;i++)
    {
        end->next=getnode(i+2);
        end=end->next;
    }
    end=head;
    while(end!=NULL)
    {
        cout<<end->val<<endl;
        end=end->next;
    }

    head=sl.swapPairs(head);
    end=head;
    cout<<"main"<<endl;
    while(end!=NULL)
    {
        cout<<end->val<<endl;
        end=end->next;
    }
#endif 
    return 0;
}

