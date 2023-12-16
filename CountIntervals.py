class CountIntervals:
    def __init__(self):
        self.intervals = []
        self.len = 0

    def add(self, left: int, right: int) -> None:
        l = 0
        r = len(self.intervals) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.intervals[mid][0] <= left:
                l = mid + 1
            else:
                r = mid - 1
        i = l

        if i > 0 and self.intervals[i - 1][1] >= left - 1:
            left = self.intervals[i - 1][0]
            right = max(self.intervals[i - 1][1], right)
            self.len -= self.intervals[i - 1][1] - self.intervals[i - 1][0] + 1
            del self.intervals[i - 1]
            i -= 1

        while i < len(self.intervals) and self.intervals[i][0] <= right + 1:
            right = max(right, self.intervals[i][1])
            self.len -= self.intervals[i][1] - self.intervals[i][0] + 1
            del self.intervals[i]
        self.intervals.insert(i, (left, right))
        self.len += self.intervals[i][1] - self.intervals[i][0] + 1

    def count(self) -> int:
        return self.len


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


opList = ["CountIntervals", "add", "add", "count", "add", "count"]
dataList = [[], [2, 3], [7, 10], [], [5, 8], []]
opList = ["CountIntervals", "count", "add", "add", "count", "count", "add"]
dataList = [[], [], [39, 44], [13, 49], [], [], [47, 50]]
Tester(opList, dataList)
