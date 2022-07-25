from collections import deque

from pytree import TreeNode


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        queue = deque([root])
        i = 0

        while i < len(queue):
            if queue[i].left is not None:
                queue.append(queue[i].left)

                if queue[i].right is not None:
                    queue.append(queue[i].right)
            i += 1

        while queue[0].left is not None and queue[0].right is not None:
            queue.popleft()
        self.queue = queue

    def insert(self, val: int) -> int:
        new = TreeNode(val)
        self.queue.append(new)

        if self.queue[0].left is None:
            self.queue[0].left = new

            return self.queue[0].val
        self.queue[0].right = new

        return self.queue.popleft().val

    def get_root(self) -> TreeNode:
        return self.root


class Tester:
    def __init__(self, opList, dataList):
        testedClass = eval(opList[0])
        testedInstance = testedClass(*dataList[0])

        for i in range(1, len(opList)):
            print(opList[i], dataList[i])

            if not dataList[i]:
                print(getattr(testedInstance, opList[i])())
            else:
                print(getattr(testedInstance, opList[i])(*dataList[i]))


opList = ["CBTInserter", "insert", "insert", "get_root"]
dataList = [[[1, 2]], [3], [4], []]
root = TreeNode.fromStrList(str(dataList[0][0]))
dataList[0][0] = root
Tester(opList, dataList)

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
