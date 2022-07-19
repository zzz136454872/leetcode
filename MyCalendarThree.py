from typing import List


class MyCalendarThree:
    def __init__(self):
        self.mem = []

    def book(self, start: int, end: int) -> int:
        self.mem.append((start, 1))
        self.mem.append((end, 0))
        self.mem.sort()
        tmp = 0
        res = 0

        for i in range(len(self.mem)):
            if self.mem[i][1] == 1:
                tmp += 1
                res = max(res, tmp)
            else:
                tmp -= 1

        return res


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


opList = ["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
dataList = [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]

Tester(opList, dataList)
