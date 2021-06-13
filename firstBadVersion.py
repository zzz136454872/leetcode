# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    return version>=start

class Solution:
    def firstBadVersion(self, n):
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if isBadVersion(mid):
                right=mid-1
            else:
                left=mid+1
        return left

start=4
n=5
sl=Solution()
print(sl.firstBadVersion(n))

