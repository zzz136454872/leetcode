
class Solution:
    def mySqrt(self, x: int) -> int:
        t=x**0.5
        if t*t>x:
            return t-1
        else:
            return t

sl=Solution()
print(sl.mySqrt(1))
