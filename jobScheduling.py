from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int],
                      profit: List[int]) -> int:
        jobs = [(startTime[i], endTime[i], profit[i])
                for i in range(len(startTime))]
        jobs.sort(key=lambda x: x[1])
        dp = [jobs[i][2] for i in range(len(jobs))]

        for i in range(len(jobs)):
            l = 0
            r = i - 1

            while l <= r:
                mid = (l + r) // 2

                if jobs[mid][1] <= jobs[i][0]:
                    l = mid + 1
                else:
                    r = mid - 1

            if r >= 0:
                dp[i] += dp[r]

            if i > 0:
                dp[i] = max(dp[i], dp[i - 1])

        return dp[-1]


startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]

print(Solution().jobScheduling(startTime, endTime, profit))
