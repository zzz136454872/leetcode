class ListNode():
    def __init__(self,count):
        self.count=count
        self.prev=None
        self.next=None
        self.ss=set()

    def insertAfter(self,node):
        node.prev=self
        node.next=self.next
        self.next.prev=node
        self.next=node

    def insertBefore(self,node):
        node.prev=self.prev
        node.next=self
        self.prev.next=node
        self.prev=node

    def remove(self):
        self.prev.next=self.next
        self.next.prev=self.prev

class AllOne:
    def __init__(self):
        self.head=ListNode(-1)
        self.head.ss.add("")
        self.tail=ListNode(-1)
        self.tail.ss.add("")
        self.head.next=self.tail
        self.tail.prev=self.head
        self.mem=dict()

    def inc(self, key: str) -> None:
        if key not in self.mem:
            if self.head.next.count==1:
                self.head.next.ss.add(key)
            else:
                newNode=ListNode(1)
                self.head.insertAfter(newNode)
            self.mem[key]=self.head.next
            self.head.next.ss.add(key)
        else:
            node=self.mem[key]
            c=node.count
            node.ss.remove(key)
            if node.next.count==c+1:
                node.next.ss.add(key)
            else:
                newNode=ListNode(c+1)
                node.insertAfter(newNode)
            node.next.ss.add(key)
            self.mem[key]=node.next
            if len(node.ss)==0:
                node.remove()

    def dec(self, key: str) -> None:
        node=self.mem[key]
        c=node.count
        node.ss.remove(key)
        if c==1:
            del self.mem[key]
        else:
            if node.prev.count==c-1:
                node.prev.ss.add(key)
            else:
                newNode=ListNode(c-1)
                node.insertBefore(newNode)
            node.prev.ss.add(key)
            self.mem[key]=node.prev
        if len(node.ss)==0:
            node.remove()

    def getMaxKey(self) -> str:
        out=self.tail.prev.ss.pop()
        self.tail.prev.ss.add(out)
        return out

    def getMinKey(self) -> str:
        out=self.head.next.ss.pop()
        self.head.next.ss.add(out)
        return out

class Tester:
    def __init__(self, opList, dataList):
        testedClass = eval(opList[0])
        testedInstance = testedClass(*dataList[0])

        for i in range(1, len(opList)):
            print(opList[i], dataList[i])

            if not dataList[i]:
                print(getattr(testedInstance, opList[i])())
            else:
                print(getattr(testedInstance, opList[i])(*dataList[i]))

opList=["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
dataList=[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Tester(opList,dataList)

