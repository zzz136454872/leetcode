/**
 * @author f4prime
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
void test()
{
    
}
#endif

#ifndef testMod


typedef struct ListNode{
    int val;
    struct ListNode *next;
} ListNode;

ListNode* getnode(int x)
{
    ListNode* out;
    out=new ListNode;
    out->next=NULL;
    out->val=x;
    return out;
}

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *t1=NULL, *t2=NULL,*t3=head;
        if(t3==NULL)
            return NULL;
        t3=t3->next;
        t2=head;
        if(t3==NULL)
            return head;
        t1=head;
        t1->next=NULL;
        t2=t3;
        t3=t3->next;
        //cout<<t3->val;

        while(t3!=NULL)
        {
            t2->next=t1;
            t1=t2;
            t2=t3;
            t3=t3->next;
            //cout<<"test"<<endl;
        }
        
        t2->next=t1;
        return t2;
    }

    void print(ListNode* p)
    {
        while(p!=NULL)
        {
            cout<<p->val<<" ";
            p=p->next;
        }
        cout<<endl;
    }
        
private:
};


#endif

int main()
{
#ifdef testMod
    test();
#endif

#ifndef testMod
    Solution sl;
    ListNode* start,*end;
    start=getnode(1);
    //end=start;
    //for(int i=2;i<=5;i++)
    //{
    //    end->next=getnode(i);
    //    end=end->next;
    //}
    sl.print(start);
    ListNode* out=sl.reverseList(start);
    sl.print(out);
    
#endif 
    return 0;
}

