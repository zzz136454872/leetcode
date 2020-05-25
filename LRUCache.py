class LRUCache(object):

    def __init__(self, capacity):
        self.mem=list()
        self.cap=capacity

    def get(self, key):
        for i in range(len(self.mem)):
            print(i,self.mem[i])
            if self.mem[i][0] == key:
                tmp=self.mem[i]
                print("tmp",tmp)
                del self.mem[i]
                self.mem.insert(0,tmp)
                print(self.mem)
                return tmp[1]
        print(self.mem)
        return -1

    def put(self, key, value):
        for i in range(len(self.mem)):
            if self.mem[i][0]==key:
                tmp=self.mem[i]
                del self.mem[i]
                tmp[1]=value
                self.mem.insert(0,tmp)
                print(self.mem)
                return 
        if self.cap == len(self.mem):
            del self.mem[-1]
        self.mem.insert(0,[key,value])
        print(self.mem)

cache=LRUCache(2)
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))
print(cache.put(3, 3))
print(cache.get(2)) 
print(cache.put(4, 4))
print(cache.get(1)) 
print(cache.get(3))
print(cache.get(4))
