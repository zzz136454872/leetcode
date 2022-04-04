from functools import reduce
from typing import List


def l2n(a):
    return ord(a) - ord('a')


class Trie:
    def __init__(self):
        self.has = False
        self.sons = [None for i in range(26)]

    def add(self, word):
        p = self

        for letter in word:
            idx = l2n(letter)

            if p.sons[idx] is None:
                p.sons[idx] = Trie()
            p = p.sons[idx]
        p.has = True


class Encrypter:
    def __init__(self, keys: List[str], values: List[str],
                 dictionary: List[str]):
        mem = {}
        rmem = {}

        for i in range(len(keys)):
            mem[keys[i]] = values[i]

            if values[i] in rmem:
                rmem[values[i]].append(keys[i])
            else:
                rmem[values[i]] = [keys[i]]
        self.mem = mem
        self.rmem = rmem
        root = Trie()

        for word in dictionary:
            root.add(word)
        self.root = root
        self.cache = {}

    def encrypt(self, word1: str) -> str:
        return reduce(lambda x, y: x + y,
                      [self.mem[letter] for letter in word1])

    def decrypt(self, word2: str) -> int:
        def decSub(node, word):
            if node is None:
                return 0

            if word == '':
                #    print('flag2')
                return 1 if node.has else 0
            out = 0
            now = word[:2]
            res = word[2:]

            for ori in self.rmem.get(now, []):
                out += decSub(node.sons[l2n(ori)], res)
            # print(word,out)

            return out

        if word2 in self.cache:
            return self.cache[word2]
        out = decSub(self.root, word2)
        self.cache[word2] = out

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


opList = ["Encrypter", "encrypt", "decrypt"]
dataList = [[['a', 'b', 'c', 'd'], ["ei", "zf", "ei", "am"],
             ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]],
            ["abcd"], ["eizfeiam"]]

# opList=["Encrypter","encrypt","decrypt"]
# dataList=[[["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"],["aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa","aa"],["abcd","acbd","adbc","badc","dacb","cadb","cbda","abad"]],["abcd"],["aaaaaaaa"]]

Tester(opList, dataList)
