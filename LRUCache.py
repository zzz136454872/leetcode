# TLE
class LRUCache1(object):
    def __init__(self, capacity):
        self.mem = list()
        self.cap = capacity

    def get(self, key):
        for i in range(len(self.mem)):
            print(i, self.mem[i])

            if self.mem[i][0] == key:
                tmp = self.mem[i]
                print("tmp", tmp)
                del self.mem[i]
                self.mem.insert(0, tmp)
                print(self.mem)

                return tmp[1]
        print(self.mem)

        return -1

    def put(self, key, value):
        for i in range(len(self.mem)):
            if self.mem[i][0] == key:
                tmp = self.mem[i]
                del self.mem[i]
                tmp[1] = value
                self.mem.insert(0, tmp)
                print(self.mem)

                return

        if self.cap == len(self.mem):
            del self.mem[-1]
        self.mem.insert(0, [key, value])
        print(self.mem)


class ListNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.mem = dict()
        self.cap = capacity
        self.front = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.front.next = self.tail
        self.tail.prev = self.front

    def get(self, key: int) -> int:
        if key not in self.mem:
            return -1
        node = self.mem[key]
        self.remove(node)
        self.insertFront(node)

        return node.val

    def insertFront(self, newNode):
        newNode.next = self.front.next
        newNode.prev = self.front
        newNode.next.prev = newNode
        self.front.next = newNode

    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next

    def put(self, key: int, value: int) -> None:
        if key in self.mem:
            self.mem[key].val = value
            newNode = self.mem[key]
            self.remove(newNode)
        else:
            newNode = ListNode(key, value)
            self.mem[key] = newNode
        self.insertFront(newNode)
        # print('mem len',len(self.mem))

        if len(self.mem) > self.cap:
            # print('del')
            del self.mem[self.tail.prev.key]
            self.remove(self.tail.prev)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)
print(cache.put(1, 1))
print(cache.put(2, 2))
print(cache.get(1))
print(cache.put(3, 3))
print(cache.get(2))
print(cache.put(4, 4))
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
