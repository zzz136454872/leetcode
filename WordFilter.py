from typing import List


class WordFilter:
    def __init__(self, words: List[str]):
        mem = {}

        for idx in range(len(words)):
            word = words[idx]

            for i in range(1, len(word) + 1):
                for j in range(len(word) - 1, -1, -1):
                    key = word[:i] + '#' + word[j:]
                    mem[key] = idx
        self.mem = mem

    def f(self, pref: str, suff: str) -> int:
        key = pref + '#' + suff

        return self.mem.get(key, -1)


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


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
opList = ["WordFilter", "f"]
dataList = [[["apple"]], ["a", "e"]]
opList = ["WordFilter", "f", "f"]
dataList = [[["i", 'c']], ["i", "i"], ["c", "c"]]
Tester(opList, dataList)
