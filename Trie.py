class TreeNode:
    def __init__(self):
        self.has = False
        self.sons = [None] * 26


def l2n(a):
    return ord(a) - ord('a')


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        p = self.root

        for letter in word:
            n = l2n(letter)

            if p.sons[n] is None:
                p.sons[n] = TreeNode()
            p = p.sons[n]
        p.has = True

    def search(self, word: str) -> bool:
        p = self.root

        for letter in word:
            n = l2n(letter)

            if p.sons[n] is None:
                return False
            p = p.sons[n]

        return p.has

    def startsWith(self, prefix: str) -> bool:
        p = self.root

        for letter in prefix:
            n = l2n(letter)

            if p.sons[n] is None:
                return False
            p = p.sons[n]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


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
    "Trie", "insert", "search", "search", "startsWith", "insert", "search"
]
dataList = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

Tester(opList, dataList)
