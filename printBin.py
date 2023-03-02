class Solution:
    def printBin(self, num: float) -> str:
        if num == 1:
            return '1'

        if num == 0:
            return '0'
        res = '0.'

        while num != 0:
            if len(res) > 32:
                return 'ERROR'

            if num >= 0.5:
                res += '1'
                num -= 0.5
            else:
                res += '0'
            num *= 2

        return res


num = 0.625
num = 0.1
print(Solution().printBin(num))
