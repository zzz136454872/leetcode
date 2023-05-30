from heapq import heappop, heappush
from typing import List, Optional

from pytree import TreeNode


# 不知道是哪个
class Solution0:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 1

        def travel(root):
            if not root:
                return -1
            # print(root.val)
            tmp = travel(root.left)

            if tmp != -1:
                return tmp
            nonlocal i

            if i == k:
                return root.val
            i += 1

            return travel(root.right)

        return travel(root)


# root = '[3,1,4,null,2]'
# k = 1
# root = '[5,3,6,2,4,null,null,1]'
# k = 3
#
# root = TreeNode.fromStrList(root)
# out = Solution().kthSmallest(root, k)
# print(out)

# 1439. 有序矩阵中的第 k 个最小数组和


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        visited = set()

        class Node:
            def __init__(self, v):
                self.v = v
                value = 0

                for i in range(len(self.v)):
                    value += mat[i][v[i]]
                self.value = value

            def __lt__(self, other):
                return self.value <= other.value

            def next(self):
                res = []

                for i in range(len(self.v)):
                    if len(mat[i]) > self.v[i] + 1:
                        res.append(self.v[:i] + (self.v[i] + 1, ) +
                                   self.v[i + 1:])

                return res

        res = 0
        v = (0, ) * len(mat)
        heap = [Node(v)]
        i = 0

        while i < k:
            now = heappop(heap)

            if now.v in visited:
                continue
            visited.add(now.v)
            i += 1

            if i == k:
                res = now.value

                break

            for nxt in now.next():
                heappush(heap, Node(nxt))

        return res


mat = [[1, 3, 11], [2, 4, 6]]
k = 5
mat = [[1, 3, 11], [2, 4, 6]]
k = 9
mat = [[1, 10, 10], [1, 4, 5], [2, 3, 6]]
k = 7
mat = [[1, 1, 10], [2, 2, 9]]
k = 7
print(Solution().kthSmallest(mat, k))
