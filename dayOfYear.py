class Solution:
    def dayOfYear(self, date: str) -> int:
        date = list(map(int, date.split('-')))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        out = sum(days[:date[1] - 1]) + date[2]

        def isLeap(y):
            return y % 400 == 0 or y % 4 == 0 and y % 100 != 0

        if isLeap(date[0]) and date[1] > 2:
            out += 1

        return out


date = "2019-01-09"
date = "2019-02-10"
date = "2003-03-01"
date = "2004-03-01"
print(Solution().dayOfYear(date))
