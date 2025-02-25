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

class Node:
    def __init__(self):
        self.size=0
        self.prev=None
        self.next=None
        self.type=0 # 0 free 1 occupied
        self.begin=0
        
class Allocator:

    def __init__(self, n: int):
        self.mem=Node()
        self.mem.size=n
        self.record={}

    def allocate(self, size: int, mID: int) -> int:
        p=self.mem
        while p!=None:
            if p.type==0 and p.size>=size:
                q = Node()
                q.type=1
                q.size=size
                q.begin=p.begin
                q.prev=p.prev
                if q.prev!=None:
                    q.prev.next=q
                else:
                    self.mem=q
                if size != p.size:
                    p.size -= size
                    p.begin += size
                    p.prev=q
                    q.next=p
                else:
                    q.next=p.next
                    if q.next!=None:
                        q.next.prev=q
                if mID not in self.record:
                    self.record[mID]=[]
                self.record[mID].append(q)
                return q.begin
            p=p.next
        return -1    
        

    def freeMemory(self, mID: int) -> int:
        res=0
        if mID in self.record:
            for node in self.record[mID]:
                res+=node.size
                node.type=0
                if node.prev!=None and node.prev.type==0:
                    node=node.prev
                if node.next!=None and node.next.type==0:
                    node.size+=node.next.size
                    if node.next.next!=None:
                        node.next.next.prev=node
                    node.next=node.next.next
                if node.next!=None and node.next.type==0:
                    node.size+=node.next.size
                    if node.next.next!=None:
                        node.next.next.prev=node
                    node.next=node.next.next
            del self.record[mID]
        return res
        

opList=["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"]
dataList=[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]
Tester(opList,dataList)
