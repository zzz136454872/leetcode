from typing import List


class TweetCounts:
    def __init__(self):
        self.mem = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        i = 0

        if tweetName not in self.mem:
            self.mem[tweetName] = []
        mem = self.mem[tweetName]

        while i < len(mem) and mem[i][0] < time:
            i += 1
        mem.insert(i, (time, tweetName))

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str,
                                   startTime: int, endTime: int) -> List[int]:
        jump = 60

        if freq == 'hour':
            jump = 3600
        elif freq == 'day':
            jump = 86400
        res = [0] * ((endTime - startTime) // jump + 1)
        mem = self.mem.get(tweetName, [])

        for tweet in mem:
            if tweet[0] < startTime:
                continue

            if tweet[0] > endTime:
                break
            loc = (tweet[0] - startTime) // jump
            res[loc] += 1

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


opList = [
    "TweetCounts", "recordTweet", "recordTweet", "recordTweet",
    "getTweetCountsPerFrequency", "getTweetCountsPerFrequency", "recordTweet",
    "getTweetCountsPerFrequency"
]
dataList = [[], ["tweet3", 0], ["tweet3", 60], ["tweet3", 10],
            ["minute", "tweet3", 0, 59], ["minute", "tweet3", 0, 60],
            ["tweet3", 120], ["hour", "tweet3", 0, 210]]

Tester(opList, dataList)
