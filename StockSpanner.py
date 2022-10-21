from typing import List


class StockSpanner:
    def __init__(self):
        self.n = 0
        self.stack = [(12345, -1)]

    def next(self, price: int) -> int:
        tmp = (price, self.n)
        self.n += 1

        while tmp >= self.stack[-1]:
            self.stack.pop()
        self.stack.append(tmp)

        return self.stack[-1][1] - self.stack[-2][1]


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


dataList = [
    "StockSpanner", "next", "next", "next", "next", "next", "next", "next"
]
opList = [[], [100], [80], [60], [70], [60], [75], [85]]
Tester(dataList, opList)
