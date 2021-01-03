class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    @classmethod
    def travel(self,head): # 从head开始遍历
        while head!=None:
            print(head.val,end=' ')
            head=head.next
        print()

