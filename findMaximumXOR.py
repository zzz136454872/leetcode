from typing import List


class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def n2s(n):
            tmp = bin(n)[2:]

            return '0' * (32 - len(tmp)) + tmp

        table = [1 << (31 - i) for i in range(32)]

        root = TreeNode()

        for num in nums:
            s = n2s(num)
            now = root

            for letter in s:
                if letter == '0':
                    if now.left is None:
                        now.left = TreeNode()
                    now = now.left
                else:
                    if now.right is None:
                        now.right = TreeNode()
                    now = now.right
        out = 0

        for num in nums:
            s = n2s(num)
            now = root
            tmp = 0

            for i in range(len(s)):
                if s[i] == '0':
                    if now.right is not None:
                        now = now.right
                        tmp += table[i]
                    else:
                        now = now.left
                else:
                    if now.left is not None:
                        now = now.left
                        tmp += table[i]
                    else:
                        now = now.right
            out = max(out, tmp)

        return out


sl = Solution()
nums = [14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]
print(sl.findMaximumXOR(nums))
