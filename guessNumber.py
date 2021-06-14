# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower,
# 1 if my number is higher, otherwise return 0
def guess(num: int) -> int:
    if num > pick:
        return 1

    if num < pick:
        return -1

    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            # print(left,right,mid)
            tmp = guess(mid)

            if tmp > 0:
                left = mid + 1
            elif tmp < 0:
                right = mid - 1
            else:
                return mid
            # print('end round',left,right,mid)

        return -1  # should never go here


n = 10
pick = 6
sl = Solution()
print(sl.guessNumber(n))
