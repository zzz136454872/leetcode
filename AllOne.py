
class ListNode():
    def __init__(count=1):
        self.key=""
        self.count=count
        self.prev=None
        self.next=None

class AllOne:
    def __init__(self):
        self.head=ListNode(-1)
        self.tail=ListNode(-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.mem=dict()

    def inc(self, key: str) -> None:
        if key not in mem:
            pass
        else:
            pass

    def dec(self, key: str) -> None:
        pass

    def getMaxKey(self) -> str:
        pass

    def getMinKey(self) -> str:
        pass


