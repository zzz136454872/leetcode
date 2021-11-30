class Solution:
    def findNthDigit(self, n: int) -> int:
        # 几位数
        # 第几个
        # 第几位
        total = 0
        i = 0

        while total < n:
            i += 1
            total += 9 * i * 10**(i - 1)
        total -= 9 * i * 10**(i - 1)
        n -= total
        base = (n - 1) // i
        shift = (n - 1) % i
        num = 10**(i - 1) + base

        return int(str(num)[shift])


n = 3
n = 11
print(Solution().findNthDigit(n))
