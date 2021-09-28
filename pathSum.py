from pytree import TreeNode


def psum(root, now, target, out):
    if root is None:
        return out
    now += root.val

    if now == target:
        out += 1
    out = psum(root.left, now, target, out)
    out = psum(root.right, now, target, out)

    return out


def pTotal(root, target):
    if root is None:
        return 0
    out = psum(root, 0, target, 0)
    out += pTotal(root.left, target)
    out += pTotal(root.right, target)

    return out


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        return pTotal(root, targetSum)


root = '[10,5,-3,3,2,null,11,3,-2,null,1]'
targetSum = 8
root = '[5,4,8,11,null,13,4,7,2,null,null,5,1]'
targetSum = 22
root = TreeNode.fromStrList(root)
print(Solution().pathSum(root, targetSum))
