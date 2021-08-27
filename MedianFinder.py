import heapq


# 数据流中的中位数
# 朴素解法
class MedianFinder1:
    def __init__(self):
        self.log = []

    def addNum(self, num: int) -> None:
        self.log.append(num)

    def findMedian(self) -> float:
        self.log.sort()

        return (self.log[len(self.log) // 2] +
                self.log[(len(self.log) - 1) // 2]) / 2


# 双堆
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []
        self.n = 0

    def addNum(self, num: int) -> None:
        self.n += 1

        if self.n == 1:
            self.small.append(-num)

            return

        if -self.small[0] < num:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)
        m = len(self.small)
        n = len(self.large)

        if m > n + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if n > m:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (self.large[0] - self.small[0]) / 2

        return float(-self.small[0])


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
