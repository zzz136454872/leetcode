class Solution:
    def romanToInt(self, s: str) -> int:
        nums = (('I', 1), ('IV', 4), ('V', 5), ('IX', 9), ('X', 10),
                ('XL', 40), ('L', 50), ('XC', 90), ('C', 100), ('CD', 400),
                ('D', 500), ('CM', 900), ('M', 1000))
        out = 0

        for i in range(len(nums) - 1, -1, -1):
            try:
                while s.index(nums[i][0]) == 0:
                    s = s[len(nums[i][0]):]
                    out += nums[i][1]
            except Exception:
                pass

        return out


sl = Solution()
s = "MCMXCIV"
print(sl.romanToInt(s))
