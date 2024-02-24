from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printTree(root):
    if root != None:
        print(root.val)
        printTree(root.left)
        printTree(root.right)


class Solution1:  #前序遍历和中序遍历
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if (len(preorder) == 0):
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


class Solution:  #中序遍历和后序遍历
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if (len(inorder) == 0):
            return None
        root = TreeNode(postorder[-1])
        #print(root.val)
        mid = inorder.index(root.val)
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid + 1:],
                                    postorder[mid:len(postorder) - 1])

        return root


postorder = [9, 15, 7, 20, 3]
inorder = [9, 3, 15, 20, 7]
sl = Solution()
printTree(sl.buildTree(inorder, postorder))
