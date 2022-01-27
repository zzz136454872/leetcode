from collections import defaultdict
from typing import List

# wa

class DetectSquares:
    def __init__(self):
        self.mem = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.mem[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        out = 0
        # print({k:dict(v) for k,v in self.mem.items()})

        for ny in self.mem[point[0]].keys():
            d = point[1] - ny
            tmp = self.mem[d + point[0]][ny] * self.mem[d + point[0]][point[1]]
            tmp += self.mem[point[0] - d][ny] * self.mem[point[0] -
                                                         d][point[1]]
            tmp *= self.mem[point[0]][ny]
            out += tmp

        return out


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)

opList = [
    "DetectSquares", "add", "add", "add", "count", "count", "add", "count"
]
dataList = [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]],
            [[11, 2]], [[11, 10]]]


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


Tester(opList, dataList)
