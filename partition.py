from typing import *
from pylist import ListNode

class Solution1:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head1=None
        head2=None
        tail1=None
        tail2=None
        while head!=None:
            tmp=head
            head=head.next
            tmp.next=None
            if tmp.val<x:
                if tail1==None:
                    tail1=tmp
                    head1=tmp
                else:
                    tail1.next=tmp
                    tail1=tmp
            else:
                if tail2==None:
                    tail2=tmp
                    head2=tmp
                else:
                    tail2.next=tmp
                    tail2=tmp
        if head1==None:
            return head2
        tail1.next=head2
        return head1

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        log=[1 for i in s]

        def isPalindrome(s):
            for i in range(len(s)//2):
                if s[i]!=s[len(s)-1-i]:
                    return False
            return True

        def cut(loc):
            if loc==len(s)-1:
                return [[s[-1]]]
            if log[loc]!=1:
                return log[loc]
            out=[]
            for i in range(loc+1,len(s)):
                if isPalindrome(s[loc:i]):
                    out.extend([[s[loc:i]]+k for k in cut(i)])
            if isPalindrome(s[loc:]):
                out.append([s[loc:]])
            log[loc]=out
            #print(loc,out)
            return out
        return cut(0)
            
sl=Solution()
# inp=ListNode(1)
# inp.next=ListNode(4)
# inp.next.next=ListNode(3)
# inp.next.next.next=ListNode(2)
# inp.next.next.next.next=ListNode(5)
# inp.next.next.next.next.next=ListNode(2)
# 
# x=3
# out=sl.partition(inp,x)
# 
# ListNode.travel(out)

s="aaaa"
print(sl.partition(s))
