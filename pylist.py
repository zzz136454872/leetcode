class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    @classmethod
    def travel(self,head): # 从head开始遍历
        if head==None:
            print('empty linked list')
        while head!=None:
            print(head.val,end=' ')
            head=head.next
        print()

    @classmethod
    def fromList(self,nums):
        virtual_head=ListNode(12345)
        p=virtual_head
        for num in nums:
            p.next=ListNode(num)
            p=p.next
        return virtual_head.next

