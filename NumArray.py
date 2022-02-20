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


if __name__ == '__main__':

    class A:
        def __init__(self, a):
            self.a = a

        def getA(self):
            return self.a

        def getB(self, b):
            return b


# 不知道是哪个
class NumArray:
    def __init__(self, nums: List[int]):
        self.pre_sum = [0]
        tmp = 0

        for num in nums:
            tmp += num
            self.pre_sum.append(tmp)

    def sumRange(self, i: int, j: int) -> int:
        return self.pre_sum[j + 1] - self.pre_sum[i]


# nums=[-2, 0, 3, -5, 2, -1]
# # Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# print(obj.sumRange(0,2))
# print(obj.sumRange(2,5))
# print(obj.sumRange(0,5))


# 307. 区域和检索 - 数组可修改
class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.c = [0] * (self.n + 1)
        self.nums = nums

        for i in range(len(nums)):
            self.add(i, nums[i])

    def lowbit(self, x):
        return x & (-x)

    def add(self, index: int, val: int) -> None:
        index += 1

        while index <= self.n:
            self.c[index] += val
            index += self.lowbit(index)

    def update(self, index: int, val: int) -> None:
        change = val - self.nums[index]
        self.add(index, change)
        self.nums[index] = val

    def s(self, r):
        r += 1
        out = 0

        while r > 0:
            out += self.c[r]
            r -= self.lowbit(r)

        return out

    def sumRange(self, left: int, right: int) -> int:
        return self.s(right) - self.s(left - 1)


opList = ["NumArray", "sumRange", "update", "sumRange"]
dataList = [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
opList = [
    "NumArray", "update", "update", "update", "sumRange", "update", "sumRange"
]
dataList = [[[7, 2, 7, 2, 0]], [4, 6], [0, 2], [0, 9], [4, 4], [3, 8], [0, 4]]
Tester(opList, dataList)
