from typing import List, Optional

from pytree import TreeNode


class Solution:
    def constructMaximumBinaryTree(self,
                                   nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        loc = nums.index(max(nums))
        root = TreeNode(nums[loc])
        root.left = self.constructMaximumBinaryTree(nums[:loc])
        root.right = self.constructMaximumBinaryTree(nums[loc + 1:])

        return root


nums = [3, 2, 1]
nums = [3, 2, 1, 6, 0, 5]
root = Solution().constructMaximumBinaryTree(nums)
TreeNode.travel(root)
