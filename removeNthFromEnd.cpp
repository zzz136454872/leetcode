/* @author f4prime
 * @email zzz136454872@163.com
 * @aim a plain model for leetcode
 */

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

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
    ListNode(int x) : val(x), next(NULL) {}
} ListNode;
 
 
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* a=head,*b=head;
        int i;
        for(i=0;i<n;i++)
        {
            a=a->next;
        }

        if(a==NULL)
        {
            return b->next;
        }
        while(a->next!=NULL)
        {
            a=a->next;
            b=b->next;
        }
        a=b->next;
        b->next=a->next;
        return head;
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

