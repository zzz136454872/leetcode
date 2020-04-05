from typing import *

def sort(a):
    for i in range(len(a)):
        change=False
        for j in range(len(a)-1):
            if a[j][2] < a[j+1][2]:
                tmp=a[j]
                a[j]=a[j+1]
                a[j+1]=tmp
                change=True
        if not change:
            break

class LFUCache:

    def __init__(self, capacity: int):
        self.cap=capacity;
        self.cache=[]

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0]==key:
                self.cache[i][2]+=1
                tmp=self.cache[i]
                del(self.cache[i])
                self.cache.insert(0,tmp)
                sort(self.cache)
                return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        #print(key,value)
        #print("flag1",self.cache)
        if self.cap==0:
            return
        for i in range(len(self.cache)):
            if self.cache[i][0]==key:
                self.cache[i][1]=value
                self.cache[i][2]+=1
                sort(self.cache)
                return
        if len(self.cache)==self.cap:
            del(self.cache[-1])
        self.cache.insert(0,[key,value,0])
        sort(self.cache)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
lfu=LFUCache(2)
lfu.put(2,1)
lfu.put(3,2)
print(lfu.get(3))
print(lfu.get(2))
lfu.put(4,3)
print(lfu.get(2))

#lfu.put(10,5)
#lfu.put(9,10)
#print(lfu.get(13))
#lfu.put(2,19)
#print(lfu.get(2))
#print(lfu.get(3))
