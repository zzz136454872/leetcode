from typing import List


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.depth = 16
        self.mem = [[-1] * self.depth for _ in range(n)]

        for i in range(n):
            self.mem[i][0] = parent[i]

        for i in range(1, self.depth):
            for j in range(n):
                if self.mem[j][i - 1] != -1:
                    self.mem[j][i] = self.mem[self.mem[j][i - 1]][i - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        tmp = node

        for i in range(self.depth):
            if (k >> i) & 1:
                tmp = self.mem[tmp][i]

                if tmp == -1:
                    return tmp

        return tmp


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


opList = ["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
dataList = [[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
Tester(opList, dataList)
