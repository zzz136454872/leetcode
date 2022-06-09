import random
from random import randint
from typing import List


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


# 黑名单中的随机数 710
class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        self.dict = {}
        self.now = 1
        blacklist = set(blacklist)
        self.length = N
        self.blacklist = blacklist
        c = 0
        whitelist = set()

        for i in range(N):
            if i not in blacklist:
                whitelist.add(i)
                c += 1

                if c > min(len(blacklist) + 1, 100000):
                    break
        back = whitelist.copy()

        for i in blacklist:
            self.dict[i] = back.pop()

            if len(back) == 0:
                back = whitelist.copy()

    def rand(self):
        self.now = (self.now * 359753) % 183389

        return self.now % self.length

    def pick(self) -> int:
        tmp = self.rand()

        if tmp in self.blacklist:
            return self.dict[tmp]

        return tmp


# sl=Solution(2,[])
# sl=Solution(1000000000, [640145908])
# for i in range(100):
#     print(sl.pick())


# 不知道是哪个
class Solution1:
    def __init__(self, N: int, blacklist: List[int]):
        blacklist = set(blacklist)
        self.blacklist = blacklist
        self.length = N

    def pick(self) -> int:
        tmp = random.randint(0, self.length - 1)

        while tmp in self.blacklist:
            tmp = (tmp + 1) % self.length

        return tmp


# 497. 非重叠矩形中的随机点
class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.mem = [0]

        for rect in rects:
            self.mem.append(self.mem[-1] + (rect[2] - rect[0] + 1) *
                            (rect[3] - rect[1] + 1))
        self.n = self.mem[-1]

    def pick(self) -> List[int]:
        a = randint(0, self.n - 1)
        left = 0
        right = len(self.mem) - 1

        while left <= right:
            mid = (left + right) // 2

            if self.mem[mid] <= a:
                left = mid + 1
            else:
                right = mid - 1
        left -= 1
        a -= self.mem[left]
        dx = self.rects[left][2] - self.rects[left][0] + 1

        return [self.rects[left][0] + a % dx, self.rects[left][1] + a // dx]


opList = ["Solution", "pick", "pick", "pick", "pick", "pick"]
dataList = [[[[-2, -2, -1, -1], [1, 0, 3, 0]]], [], [], [], [], []]
opList = ["Solution", "pick", "pick", "pick", "pick", "pick"]
dataList = [[[[-2, -2, 1, 1], [2, 2, 4, 6]]], [], [], [], [], []]
Tester(opList, dataList)
