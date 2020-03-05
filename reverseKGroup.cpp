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
    ListNode* reverseKGroup(ListNode* head, int k) {
        list=new ListNode*[k];
        if(head==NULL)
            return NULL;
        ListNode *tmp0=head,*tmpk;

        for(int i=0;i<k;i++)
        {
            list[i]=tmp0;
            tmp0=tmp0->next;
            if(tmp0==NULL&&i!=k-1)
                return head;
        }
        
        for(int i=0;i<k-1;i++)
        {
            list[i+1]->next=list[i];
        }

        list[0]->next=tmp0;
        head=list[k-1];
        
        while(true)
        {
            tmp0=list[0];
            for(int i=0;i<k;i++)
            {
                if(i==0)
                    list[0]=tmp0->next;
                else
                    list[i]=list[i-1]->next;
                if(list[i]==NULL)
                    return head;
            }
            tmpk=list[k-1]->next;
            for(int i=0;i<k-1;i++)
            {
                list[i+1]->next=list[i];
            }
            tmp0->next=list[k-1];
            list[0]->next=tmpk;
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

private:
    ListNode** list;
    
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
    for(int i=0;i<1;i++)
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

    head=sl.reverseKGroup(head,2);
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

