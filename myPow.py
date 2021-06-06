class Solution1:
    def myPow(self, x: float, n: int) -> float:
        return float(x**n)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        out = 1

        if n > 0:
            tmp = x
        else:
            tmp = 1 / x

        while n != 0:

            if n % 2 != 0:
                out *= tmp

            if n > 0:
                n = n // 2
            else:
                n = -((-n) // 2)
            tmp *= tmp

        return out


sl = Solution()
x = 2.00000
n = 10
x = 2.10000
n = 3
x = 2.00000
n = -2
print(sl.myPow(x, n))
