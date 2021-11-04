class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = 1234567

        while left <= right:
            mid = (left + right) // 2

            if mid**2 >= num:
                right = mid - 1
            else:
                left = mid + 1

        return left**2 == num


num = 14
print(Solution().isPerfectSquare(num))
