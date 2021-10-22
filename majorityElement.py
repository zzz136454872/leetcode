from typing import List


# 求众数1
class Solution1:
    def majorityElement(self, nums):
        log = dict()

        for num in nums:
            if num in log.keys():
                log[num] += 1
            else:
                log[num] = 0

        for key in log.keys():
            if log[key] >= len(nums) / 2:
                return key

        return 0


# 求众数2
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major = []
        count = []

        for num in nums:
            find = False

            for i in range(len(major)):
                if num == major[i]:
                    count[i] += 1
                    find = True

            if find:
                continue

            if len(major) < 2:
                count.append(1)
                major.append(num)

                continue
            count[1] -= 1

            if count[1] == 0:
                del count[1]
                del major[1]
            count[0] -= 1

            if count[0] == 0:
                del count[0]
                del major[0]
        out = []

        for num in major:
            if nums.count(num) > len(nums) // 3:
                out.append(num)

        return out

nums=[1,1,2,3,4]
print(Solution().majorityElement(nums))


# 主要元素
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        now = -1
        now_count = 0

        for num in nums:
            if num == now:
                now_count += 1

                continue

            if now_count == 0:
                now = num
                now_count = 1

                continue
            now_count -= 1

        if nums.count(now) > len(nums) // 2:
            return now

        return -1


# sl = Solution()
# inp = [1, 1, 1, 3, 3, 2, 2, 2]
# inp = [1, 2, 5, 9, 5, 9, 5, 5, 5]
# inp = [3, 2]
# inp = [2, 2, 1, 1, 1, 2, 2]
# inp = [1, 2, 3]
# print(sl.majorityElement(inp))
