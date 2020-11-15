import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        k=minutesToTest//minutesToDie
        x=math.log(buckets,k+1)
        return math.ceil(x)

sl=Solution()
print(sl.poorPigs(1000,15,60))
