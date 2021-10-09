from typing import *


# 不知道是哪一个
class Solution1:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []

        if len(nums) == 0:
            return out
        pre = nums[0]
        pre_start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != pre + 1:
                if pre_start == pre:
                    out.append(str(pre))
                else:
                    out.append(str(pre_start) + '->' + str(pre))
                pre_start = nums[i]
            pre = nums[i]

        if pre_start == pre:
            out.append(str(pre))
        else:
            out.append(str(pre_start) + '->' + str(pre))

        return out


# nums = [0,1,2,4,5,7]
# nums = [0,2,3,4,6,8,9]
# sl=Solution()
# print(sl.summaryRanges(nums))

# 将数据流变为多个不相交区间


class SummaryRanges:
    def __init__(self):
        self.log = [[-2, -2], [123456, 123456]]

    def addNum(self, val: int) -> None:
        # print('before', self.log)
        left = 0
        right = len(self.log) - 1

        while left <= right:
            mid = (left + right) // 2

            if val >= self.log[mid][0]:
                left = mid + 1
            else:
                right = mid - 1
        # print('search', left)

        if val <= self.log[left - 1][1]:
            return

        if val == self.log[left - 1][1] + 1:
            self.log[left - 1][1] += 1

            if self.log[left - 1][1] == self.log[left][0] - 1:
                self.log[left - 1][1] = self.log[left][1]
                del self.log[left]

            return

        if val == self.log[left][0] - 1:
            self.log[left][0] -= 1

            return
        self.log.insert(left, [val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.log[1:len(self.log) - 1]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

opList = [
    "SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
    "addNum", "getIntervals", "addNum", "getIntervals", "addNum",
    "getIntervals"
]
dataList = [[], [1], [], [3], [], [7], [], [2], [], [6], []]

# opList=["SummaryRanges", "addNum",  "addNum",  "addNum", "getIntervals"]
# dataList=[[], [1], [3], [2], []]


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
