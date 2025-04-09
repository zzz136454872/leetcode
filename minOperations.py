from typing import List


# 1769. 移动所有球到每个盒子所需的最小操作数
class Solution1:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(i) for i in boxes]
        left = [0 for i in boxes]
        right = [0 for i in boxes]
        tmp = 0

        for i in range(len(boxes)):
            left[i] = tmp
            tmp += boxes[i]
        tmp = 0

        for i in range(len(boxes) - 1, -1, -1):
            right[i] = tmp
            tmp += boxes[i]
        tmp = 0

        for i in range(len(boxes)):
            if boxes[i]:
                tmp += i
        out = [tmp]
        # print(left, right)

        for i in range(1, len(boxes)):
            tmp += left[i] - right[i - 1]
            out.append(tmp)

        return out


# boxes = "110"
# boxes = "001011"
# sl = Solution()
# print(sl.minOperations(boxes))


# 得到子序列的最少操作次数
class Solution2:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        mem = {}

        for i in range(len(target)):
            mem[target[i]] = i
        arr1 = []

        for num in arr:
            if num in mem:
                arr1.append(mem[num])

        if len(arr1) == 0:
            return len(target)
        stack = [arr1[0]]
        lcs = 1

        for num in arr1[1:]:
            if num > stack[-1]:
                stack.append(num)
                lcs = max(lcs, len(stack))
            else:
                left = 0
                right = len(stack) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if stack[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                lcs = max(lcs, left + 1)
                stack[left] = num

        return len(target) - lcs


# sl = Solution()
#
# target = [5, 1, 3]
# arr = [9, 4, 2, 3, 4]
#
# target = [6, 4, 8, 1, 3, 2]
# arr = [4, 7, 6, 2, 3, 8, 6, 1]

# print(sl.minOperations(target, arr))


# 不知道是哪个
class Solution3:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            if log == '../':
                if depth > 0:
                    depth -= 1
            elif log == './':
                continue
            else:
                depth += 1

        return depth


# logs = ["d1/", "d2/", "../", "d21/", "./"]
# print(Solution().minOperations(logs))


# 1758. 生成交替二进制字符串的最少操作数
class Solution4:
    def minOperations(self, s: str) -> int:
        c1 = 0
        c2 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    c1 += 1
                else:
                    c2 += 1
            else:
                if s[i] == '0':
                    c2 += 1
                else:
                    c1 += 1
        print(c1, c2)

        return min(c1, c2)


# s = "0100"
# print(Solution().minOperations(s))


# 1775. 通过最少操作次数使数组的和相等
class Solution5:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        s1 = sum(nums1)
        s2 = sum(nums2)

        if s1 > s2:
            s1, s2 = s2, s1
            nums1, nums2 = nums2, nums1
        diff = s2 - s1

        if diff == 0:
            return 0
        # print(nums1,nums2,diff)
        i = 0
        j = len(nums2) - 1
        res = 0

        while True:
            res += 1
            d1 = 0
            d2 = 0

            if i < len(nums1):
                d1 = 6 - nums1[i]
                # print('d1',d1)

            if j >= 0:
                d2 = nums2[j] - 1
                # print('d2',d2)

            if d1 > d2:
                i += 1
                d = d1
            else:
                j -= 1
                d = d2

            if d >= diff:
                return res

            if d == 0:
                return -1
            diff -= d
            # print(i,j,d,diff)

        return -1


# nums1 = [1, 2, 3, 4, 5, 6]
# nums2 = [1, 1, 2, 2, 2, 2]
# nums1 = [1, 1, 1, 1, 1, 1, 1]
# nums2 = [6]
# nums1 = [6, 6]
# nums2 = [1]
# nums1 = [5, 6, 4, 3, 1, 2]
# nums2 = [6, 3, 3, 1, 4, 5, 3, 4, 1, 3, 4]
# print(Solution().minOperations(nums1, nums2))


# 不知道是哪个
class Solution6:
    def minOperations(self, nums: List[int]) -> int:
        res = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                res += nums[i - 1] + 1 - nums[i]
                nums[i] = nums[i - 1] + 1

        return res


# nums = [1, 1, 1]
# nums = [1, 5, 2, 4, 1]
# nums = [8]
# print(Solution().minOperations(nums))


# 将 x 减到 0 的最小操作数
class Solution7:
    def minOperations(self, nums: List[int], x: int) -> int:
        if x == 0:
            return 0
        s = sum(nums)
        t = s - x
        tmp = 0
        res = len(nums) + 1
        j = 0

        for i in range(len(nums)):
            while j < len(nums) and tmp < t:
                tmp += nums[j]
                j += 1

            if tmp == t:
                res = min(res, len(nums) - (j - i))
            tmp -= nums[i]

        return res if res != len(nums) + 1 else -1


# nums = [1, 1, 4, 2, 3]
# x = 5
# nums = [5, 6, 7, 8, 9]
# x = 4
# nums = [3, 2, 20, 1, 1, 3]
# x = 10
# print(Solution().minOperations(nums, x))


# 1551. 使数组中所有元素相等的最小操作数
class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return n**2 // 4

        return (n + 1) * (n - 1) // 4


n = 3
n = 6
print(Solution().minOperations(n))


# 3375. 使数组的值全部为 K 的最少操作次数
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mem = set()

        for num in nums:
            if num < k:
                return -1
            mem.add(num)
        mem.discard(k)

        return len(mem)
