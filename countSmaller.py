from typing import *


# 315. 计算右侧小于当前元素的个数
# 8000ms
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        log = []
        out = []

        for i in range(len(nums) - 1, -1, -1):
            left = 0
            right = len(log) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[i] <= log[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            out.insert(0, len(log) - left)
            log.insert(left, nums[i])

        return out

# 315. 计算右侧小于当前元素的个数
# 1700ms
def lowbit(x):
    return x&(-x)

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        move=10**4+1
        out=[]
        self.mem=[0]*(2*move)
        self.n=2*move-1
        for i in range(len(nums)-1,-1,-1):
            out.append(self.query(nums[i]+move-1))
            self.add(nums[i]+move)
        return out[::-1]

    def add(self,x):
        while x<=self.n:
            self.mem[x]+=1
            x+=lowbit(x)

    def query(self,x):
        out=0
        while x>0:
            out+=self.mem[x]
            x-=lowbit(x)
        return out

nums = [5, 2, 6, 1]
nums = [1,1,1, 1]
sl = Solution()
print(sl.countSmaller(nums))
