# 学生出勤记录
class Solution1:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and 'LLL' not in s


class Solution:
    def checkRecord(self, n: int) -> int:
        nAnL = 1
        nAL = 1
        nALL = 0
        AnL = 1
        AL = 0
        ALL = 0
        mod = 10**9 + 7

        for i in range(n - 1):
            newnAnL = (nAnL + nAL + nALL) % mod
            newnAL = nAnL
            newnALL = nAL
            newAnL = (nAnL + nAL + nALL + AnL + AL + ALL) % mod
            newAL = AnL
            newALL = AL
            nAnL = newnAnL
            nAL = newnAL
            nALL = newnALL
            AnL = newAnL
            AL = newAL
            ALL = newALL

        return (nAnL + nAL + nALL + AnL + AL + ALL) % mod


sl = Solution()
n = 2
n = 10101
print(sl.checkRecord(n))
