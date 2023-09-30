from typing import List

from pytree import TreeNode


# 不知道是哪个
class Solution1:
    def rob(self, nums: List[int]) -> int:
        log = [0 for i in range(len(nums))]
        m = 0

        for i in range(len(nums)):
            if i <= 1:
                log[i] = nums[i]
            else:
                log[i] = nums[i] + max(log[:i - 1])
            m = max(m, log[i])

        return m


# inp=[2,1,1,2]
# sl=Solution()
# print(sl.rob(inp))


def sum1(a):
    if a in sum1.log.keys():
        return sum1.log[a]

    if a == None:
        sum1.log[a] = 0

        return 0
    add1 = a.val + sum2(a.left) + sum2(a.right)
    add2 = sum1(a.left) + sum1(a.right)
    m = max(add1, add2)
    sum1.log[a] = m

    return m


def sum2(a):
    if a in sum2.log.keys():
        return sum2.log[a]

    if a == None:
        sum2.log[a] = 0

        return 0
    m = sum1(a.left) + sum1(a.right)
    sum2.log[a] = m

    return m


# 不知道是哪个
class Solution2:
    def rob(self, root: TreeNode) -> int:
        sum1.log = {}
        sum2.log = {}

        return sum1(root)


# sl=Solution()
# root=TreeNode(3)
# root.left=TreeNode(4)
# root.right=TreeNode(5)
# root.left.left=TreeNode(1)
# root.left.right=TreeNode(3)
# root.right.right=TreeNode(1)
# print(sl.rob(root))


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        res = 0
        mem = [nums[0], nums[1]]

        for i in range(2, len(nums)):
            mem
        res = max(mem)
        t = mem[0]
        del nums[0]
        nums.append(t)
        mem = [nums[0], nums[1]]

        for i in range(2, len(nums)):
            mem
        res = max(res, max(mem))

        return res


nums = [2, 3, 2]
nums = [1, 2, 3, 1]
print(Solution().rob(nums))
