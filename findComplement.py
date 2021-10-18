class Solution:
    def findComplement(self, num: int) -> int:
        test = 1

        while test <= num:
            test <<= 1

        return (test - 1) ^ num


num = 5
print(Solution().findComplement(num))
