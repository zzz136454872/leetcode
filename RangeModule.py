from typing import *

# wrong answer
class RangeModule:
    def __init__(self):
        self.store = []

    def bsearch(self, r):
        start = 0
        end = len(self.store) - 1

        while start <= end:
            mid = (start + end) // 2
            now = self.store[mid]

            if now == r:
                return mid
            elif now > r:
                end = mid - 1
            else:
                start = mid + 1

        return start

    def merge(self, a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]

    def addRange(self, left: int, right: int) -> None:
        rang = [left, right]
        i = self.bsearch(rang)

        if i > 0 and self.store[i - 1][1] >= rang[0]:
            rang = self.merge(self.store[i - 1], rang)
            del self.store[i - 1]
            i -= 1

        while i < len(self.store) and rang[1] >= self.store[i][0]:
            rang = self.merge(self.store[i], rang)
            del self.store[i]
        self.store.insert(i, rang)
        print(self.store)

    def queryRange(self, left: int, right: int) -> bool:
        i = self.bsearch([left, right])

        if i > 0 and self.store[i - 1][1] >= right:
            return True

        if i < len(self.store) and self.store[i][0] == left:
            return True

        return False

    def sub(self, a, b):
        res = []

        if a[0] >= b[1] or a[1] <= b[0]:
            return [a]

        if a[0] < b[0]:
            res.append([a[0], b[0]])

        if a[1] > b[1]:
            res.append([b[1], a[1]])

        return res

    def removeRange(self, left: int, right: int) -> None:
        rang = [left, right]
        i = self.bsearch(rang)
        # print(rang,i,self.store)

        if i > 0:
            tmp = self.sub(self.store[i - 1], rang)
            del self.store[i - 1]

            if len(tmp) > 0:
                self.store.insert(i - 1, tmp[0])

                if len(tmp) == 2:
                    i += 1
                    self.store.insert(i - 1, tmp[1])

        while i < len(self.store) and right > self.store[i][0]:
            if right >= self.store[i][1]:
                del self.store[i]
            else:
                self.store[i][0] = right
        print(self.store)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)


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
    "RangeModule", "addRange", "removeRange", "queryRange", "queryRange",
    "queryRange"
]
dataList = [[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]

opList = [
    "RangeModule", "addRange", "addRange", "addRange", "queryRange",
    "queryRange", "queryRange", "removeRange", "queryRange"
]
dataList = [[], [10, 180], [150, 200], [250, 500], [50, 100], [180, 300],
            [600, 1000], [50, 150], [50, 100]]

opList = [
    "RangeModule", "addRange", "queryRange", "removeRange", "removeRange",
    "addRange", "queryRange", "addRange", "queryRange", "removeRange"
]
dataList = [[], [5, 8], [3, 4], [5, 6], [3, 6], [1, 3], [2, 3], [4, 8], [2, 3],
            [4, 9]]

opList = [
    "RangeModule", "addRange", "removeRange", "removeRange", "addRange",
    "removeRange", "addRange", "queryRange", "queryRange", "queryRange"
]
dataList = [[], [6, 8], [7, 8], [8, 9], [8, 9], [1, 3], [1, 8], [2, 4], [2, 9],
            [4, 6]]

opList = [
    "RangeModule", "addRange", "removeRange", "queryRange", "queryRange",
    "queryRange", "removeRange", "removeRange", "removeRange", "addRange",
    "addRange", "addRange", "removeRange", "addRange", "queryRange",
    "addRange", "addRange", "queryRange", "queryRange", "addRange",
    "removeRange", "removeRange", "removeRange", "queryRange", "queryRange",
    "addRange", "addRange", "queryRange", "addRange", "addRange",
    "removeRange", "addRange", "addRange", "queryRange", "removeRange",
    "queryRange", "removeRange", "addRange", "addRange", "queryRange",
    "removeRange", "removeRange", "addRange", "queryRange", "queryRange",
    "removeRange", "removeRange", "removeRange", "queryRange", "addRange",
    "removeRange", "removeRange", "queryRange", "removeRange", "removeRange",
    "queryRange", "addRange", "addRange", "removeRange", "queryRange",
    "queryRange", "addRange", "removeRange", "removeRange", "addRange",
    "addRange", "addRange", "addRange", "queryRange", "removeRange",
    "addRange", "addRange", "addRange", "queryRange", "addRange",
    "removeRange", "queryRange", "removeRange", "removeRange", "removeRange",
    "queryRange", "queryRange", "queryRange", "queryRange", "queryRange",
    "removeRange", "queryRange", "removeRange", "queryRange", "addRange",
    "queryRange"
]
dataList = [[], [14, 100], [1, 8], [77, 80], [8, 43], [4, 13],
            [3, 9], [45, 49], [41, 90], [58, 79], [4, 83], [34, 39], [84, 100],
            [8, 9], [32, 56], [35, 46], [9, 100], [85, 99], [23, 33], [10, 31],
            [15, 45], [52, 70], [26, 42], [30, 70], [60, 69], [10,
                                                               94], [2, 89],
            [26, 39], [46, 93], [30, 83], [42, 48], [47, 74], [39,
                                                               45], [14, 64],
            [3, 97], [16, 34], [28, 100], [19, 37], [27, 91], [55,
                                                               62], [64, 65],
            [2, 48], [55, 78], [21, 89], [31, 76], [13, 32], [2, 84], [21, 88],
            [12, 31], [89, 97], [56, 72], [16, 75], [18, 90], [46,
                                                               60], [20, 62],
            [28, 77], [5, 78], [58, 61], [38, 70], [24, 73], [72, 96], [5, 24],
            [43, 49], [2, 20], [4, 69], [18, 98], [26, 42], [14, 18], [46, 58],
            [16, 90], [32, 47], [19, 36], [26, 78],
            [7, 58], [42, 54], [42, 83], [3, 83], [54, 82], [71, 91], [22, 37],
            [38, 94], [20, 44], [37, 89], [15, 54], [1, 64], [63,
                                                              65], [55, 58],
            [23, 44], [25, 87], [38, 85], [27, 71]]

Tester(opList, dataList)
