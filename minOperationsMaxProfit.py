from typing import List


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int,
                               runningCost: int) -> int:
        maxTime = -1
        maxValue = 0
        time = 0
        value = 0
        waiting = 0

        for customer in customers:
            time += 1
            waiting += customer
            value -= runningCost
            running = min(waiting, 4)
            waiting -= running
            value += boardingCost * running

            if value > maxValue:
                maxValue = value
                maxTime = time

        while waiting > 0:
            time += 1
            value -= runningCost
            running = min(waiting, 4)
            waiting -= running
            value += boardingCost * running

            if value > maxValue:
                maxValue = value
                maxTime = time

        return maxTime


customers = [8, 3]
boardingCost = 5
runningCost = 6
customers = [10, 9, 6]
boardingCost = 6
runningCost = 4
customers = [3, 4, 0, 5, 1]
boardingCost = 1
runningCost = 92
print(Solution().minOperationsMaxProfit(customers, boardingCost, runningCost))
