from typing import *


class Node:
    def __init__(self, value):
        self.son = [None for i in range(26)]
        self.value = value

    def print(self):
        print(self.value, ':', end=' ')

        for i in range(len(self.son)):
            print(chr(ord('a') + i), self.son[i], end='')


class MapSum:
    def __init__(self):
        self.root = Node(0)

    def insert(self, key: str, val: int) -> None:
        root = self.root

        for letter in key:
            num = ord(letter) - ord('a')

            if root.son[num] == None:
                root.son[num] = Node(0)
            root = root.son[num]
        root.value = val
        #print(root.value)

    def sum(self, prefix: str) -> int:
        root = self.root

        for letter in prefix:
            num = ord(letter) - ord('a')

            if root.son[num] == None:
                print('false')

                return 0
            root = root.son[num]

        return self.son_sum(root)

    def son_sum(self, root):
        if root == None:
            return 0
        out = root.value

        for i in range(26):
            out += self.son_sum(root.son[i])

        return out


obj = MapSum()
obj.insert("apple", 3)
print(obj.sum("ap"))
obj.insert("app", 2)
print(obj.sum("ap"))
