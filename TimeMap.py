class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mem:
            self.mem[key].append((timestamp, value))
        else:
            self.mem[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mem:
            return ""
        lis = self.mem[key]
        l = 0
        r = len(lis) - 1

        while l <= r:
            m = (l + r) // 2

            if lis[m][0] > timestamp:
                r = m - 1
            else:
                l = m + 1

        if l == 0:
            return ""

        return lis[l - 1][1]


# Your TimeMap object will be instantiated and called as such:

ops = ["TimeMap", "set", "get", "get", "set", "get", "get"]
data = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4],
        ["foo", 4], ["foo", 5]]

ops = ["TimeMap", "set", "set", "get", "get", "get", "get", "get"]
data = [[], ["love", "high", 10], ["love", "low", 20], ["love", 5],
        ["love", 10], ["love", 15], ["love", 20], ["love", 25]]


class Tester:
    def __init__(self, opList, dataList):
        testedClass = eval(opList[0])
        testedInstance = testedClass(*dataList[0])

        for i in range(1, len(opList)):
            print(opList[i], dataList[i])

            if not dataList[i][0]:
                print(getattr(testedInstance, opList[i])())
            else:
                print(getattr(testedInstance, opList[i])(*dataList[i]))


Tester(ops, data)
