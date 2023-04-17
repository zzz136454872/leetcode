class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def parseDate(s):
            d = list(map(int, s.split('-')))
            d[0] -= 1
            res = d[1]

            for i in range(d[0]):
                res += days[i]

            return res

        aa = parseDate(arriveAlice)
        la = parseDate(leaveAlice)
        ab = parseDate(arriveBob)
        lb = parseDate(leaveBob)

        return max(0, min(la, lb) - max(aa, ab) + 1)


arriveAlice = "08-15"
leaveAlice = "08-18"
arriveBob = "08-16"
leaveBob = "08-19"
arriveAlice = "10-01"
leaveAlice = "10-31"
arriveBob = "11-01"
leaveBob = "12-31"

print(Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob,
                                   leaveBob))
