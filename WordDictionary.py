from typing import List


class Trie:
    def __init__(self):
        self.has = False
        self.sons = [None for i in range(26)]


def l2n(a):
    return ord(a) - ord('a')

class WordDictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        now = self.root

        for letter in word:
            n = l2n(letter)

            if now.sons[n] is None:
                now.sons[n] = Trie()
            now = now.sons[n]
        now.has = True

    def search(self, word: str) -> bool:
        def search_sub(root, loc):
            if root is None:
                return False

            if loc == len(word):
                if root.has:
                    return True

                return False

            if word[loc] == '.':
                for i in range(26):
                    if search_sub(root.sons[i], loc + 1):
                        return True

                return False

            if search_sub(root.sons[l2n(word[loc])], loc + 1):
                return True

            return False

        return search_sub(self.root, 0)


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


opList = [
    "WordDictionary", "addWord", "addWord", "addWord", "search", "search",
    "search", "search"
]
dataList = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]

Tester(opList, dataList)
