from typing import List


# 不知道是哪个
class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = dict()

        for num in nums1:
            if num in dict1.keys():
                dict1[num] += 1
            else:
                dict1[num] = 1
        dict2 = dict()

        for num in nums2:
            if num in dict2.keys():
                dict2[num] += 1
            else:
                dict2[num] = 1

        out = []

        for num in dict1.keys():
            if num in dict2.keys():
                out.extend([num] * min(dict1[num], dict2[num]))

        return out


# sl=Solution()
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# print(sl.intersect(nums1,nums2))
"""
# Definition for a QuadTree node.
"""


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft,
                 bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            if quadTree1.val == 1:
                return quadTree1

            return quadTree2

        if quadTree2.isLeaf:
            if quadTree2.val == 1:
                return quadTree2

            return quadTree1
        res = Node(0, False, None, None, None, None)
        res.topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        res.topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        res.bottomLeft = self.intersect(quadTree1.bottomLeft,
                                        quadTree2.bottomLeft)
        res.bottomRight = self.intersect(quadTree1.bottomRight,
                                         quadTree2.bottomRight)

        if res.topRight.isLeaf and res.topLeft.isLeaf and res.bottomLeft.isLeaf and res.bottomRight.isLeaf and res.topRight.val == res.topLeft.val and res.topRight.val == res.bottomLeft.val and res.topRight.val == res.bottomRight.val:
            res.val = res.topRight.val
            res.isLeaf = True
            res.topRight = None
            res.topLeft = None
            res.bottomLeft = None
            res.bottomRight = None

        return res
