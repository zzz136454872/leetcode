from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.m = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.m = max(self.m, self.freq[val])
        self.group[self.freq[val]].append(val)

    def pop(self) -> int:
        val = self.group[self.m].pop()

        if len(self.group[self.m]) == 0:
            self.m -= 1
        self.freq[val] -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()


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
    "FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop",
    "pop", "pop"
]
dataList = [[], [5], [7], [5], [7], [4], [5], [], [], [], []]

Tester(opList, dataList)
