class Node:
    def __init__(self,k,v,f):
        self.k=k
        self.v=v
        self.f=f
        self.prev=None
        self.nxt=None

class LFUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.data={}
        self.mem={}
        self.min=0
        
    def get(self, key: int) -> int:
        if key in self.data:
            d=self.data[key]
            self.remove(d)
            if self.min==d.f and self.mem[d.f][0].nxt==self.mem[d.f][1]:
                self.min+=1
            d.f+=1
            self.insert(d)
            return d.v
        return -1
    
    def remove(self,d):
        p=d.prev
        n=d.nxt
        p.nxt=n
        n.prev=p

    def insert(self,d):
        if d.f not in self.mem:
            head=Node(-1,-1,-1)
            tail=Node(-1,-1,-1)
            head.nxt=tail
            tail.prev=head
            self.mem[d.f]=[head,tail]
        h=self.mem[d.f][0]
        n=h.nxt
        h.nxt=d
        d.prev=h
        d.nxt=n
        n.prev=d

    def put(self, key: int, value: int) -> None:
        if key==7 and value==22:
            print('flag')
        if self.cap==0:
            return
        if key in self.data:
            d=self.data[key]
            d.v=value
            self.remove(d)
            d.f+=1
            self.insert(d)
        else:
            if len(self.data)==self.cap:
                d=self.mem[self.min][1].prev
                self.remove(d)
                del self.data[d.k]
            self.min=1
            d=Node(key,value,1)
            self.data[key]=d
            self.insert(d)

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


opList=["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
dataList=[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
opList=["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]

dataList=[[2],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
Tester(opList,dataList)

