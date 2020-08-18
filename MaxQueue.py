class MaxQueue0:

    def __init__(self):
        self.max_int=-1
        self.max_count=0
        self.queue=[]

    def max_value(self) -> int:
        return self.max_int

    def push_back(self, value: int) -> None:
        if self.max_count==0:
            self.max_int=value
        if self.max_int==value:
            self.max_count+=1
        elif self.max_int < value:
            self.max_int=value
            self.max_count=1
        self.queue.append(value)
            
    def pop_front(self) -> int:
        if len(self.queue)==0:
            return -1
        else:
            out=self.queue[0]
            self.queue=self.queue[1:]
            if out==self.max_int:
                self.max_count-=1
                if len(self.queue)==0:
                    self.max_int=-1
                elif self.max_count==0:
                    self.max_int=max(self.queue)
                    self.max_count=self.queue.count(self.max_int)
            return out

# q=MaxQueue()
# print(q.push_back(1))
# print(q.pop_front())
# print(q.max_value())

# 另一种解决方法
class MaxQueue:
    def __init__(self):
        self.queue=[]
        self.maxQueue=[]

    def max_value(self) -> int:
        if self.maxQueue:
            return self.maxQueue[0]
        else:
            return -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        i=0
        while i<len(self.maxQueue):
            if self.maxQueue[i]<value:
                del self.maxQueue[i]
            else:
                i+=1
        self.maxQueue.append(value)

    def pop_front(self) -> int:
        if self.queue:
            v=self.queue.pop(0)
            if v==self.maxQueue[0]:
                del self.maxQueue[0]
        else:
            v=-1
        return v
            
q=MaxQueue()
print(q.push_back(15))
print(q.max_value())
print(q.push_back(9))
print(q.max_value())
#print(q.pop_front())

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
