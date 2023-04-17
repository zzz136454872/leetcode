import bisect
from collections import defaultdict
from random import randint
from typing import List


class MajorityChecker:
    def __init__(self, arr: List[int]):
        mem = defaultdict(list)

        for i in range(len(arr)):
            mem[arr[i]].append(i)
        self.mem = mem
        self.arr = arr

    def query(self, left: int, right: int, threshold: int) -> int:
        checked = set()

        for i in range(20):
            idx = randint(left, right)
            v = self.arr[idx]

            if v in checked:
                continue
            checked.add(v)
            l = bisect.bisect_left(self.mem[v], left)
            r = bisect.bisect_right(self.mem[v], right)

            if r - l >= threshold:
                return v

        return -1


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


opList = ["MajorityChecker", "query", "query", "query"]
dataList = [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
print(Tester(opList, dataList))
