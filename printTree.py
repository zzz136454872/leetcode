from typing import List, Optional

from pytree import TreeNode


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        tmp = [root]
        res = []

        while any(tmp):
            ntmp = []
            nres = []

            for line in res:
                nres.append([])

                for i in range(len(line)):
                    nres[-1].append('')
                    nres[-1].append(line[i])
                nres[-1].append('')

            nres.append([])

            for node in tmp:
                if node is None:
                    nres[-1].append('')
                    ntmp.extend((None, 0, None))
                elif node == 0:
                    ntmp.append(0)
                    nres[-1].append('')
                else:
                    nres[-1].append(str(node.val))
                    ntmp.append(node.left)
                    ntmp.append(0)
                    ntmp.append(node.right)
            res = nres
            tmp = ntmp

        return res


root = '[1,2]'
root = '[1,2,3,null,4]'
root = TreeNode.fromStrList(root)
print(Solution().printTree(root))
