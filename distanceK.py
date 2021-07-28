from typing import List

from pytree import TreeNode


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adjTable = [[] for i in range(501)]

        def dfs(root):
            if root is None:
                return

            if root.left is not None:
                adjTable[root.val].append(root.left.val)
                adjTable[root.left.val].append(root.val)
                dfs(root.left)

            if root.right is not None:
                adjTable[root.val].append(root.right.val)
                adjTable[root.right.val].append(root.val)
                dfs(root.right)
        dfs(root)

        distance = [2000] * 501
        tr = target.val
        distance[tr] = 0
        queue = [tr]

        while len(queue) > 0 and distance[queue[0]] < k:
            now = queue.pop(0)
            dis = distance[now]
            # print('now',now,'dis',dis,'queue',queue)

            for num in adjTable[now]:
                # print('num',num)
                if distance[num] > dis:
                    distance[num] = dis + 1
                    queue.append(num)
        out = []

        for i in range(501):
            if distance[i] == k:
                out.append(i)

        # print(adjTable[:10])
        # print(distance[:10])
        return out



sl = Solution()
root = '[3,5,1,6,2,0,8,null,null,7,4]'
target = 5
K = 2
root = TreeNode.fromStrList(root)
target = root.searchNode(target)
print(target.val)
print(sl.distanceK(root, target, K))
