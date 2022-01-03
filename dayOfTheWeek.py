from typing import List


class Solution:
    def isLeap(self, y):
        return y % 400 == 0 or y % 4 == 0 and y % 100 != 0

    def dayOfYear(self, date: List[int]) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        out = sum(days[:date[1] - 1]) + date[2]

        if self.isLeap(date[0]) and date[1] > 2:
            out += 1

        return out

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        base = 4
        weekDay = [
            "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday"
        ]

        for i in range(1971, year):
            base += 365 if not self.isLeap(i) else 366
        base += self.dayOfYear([year, month, day])

        return weekDay[base % 7]


day = 31
month = 8
year = 2019
day = 18
month = 7
year = 1999
day = 15
month = 8
year = 1993
print(Solution().dayOfTheWeek(day, month, year))
