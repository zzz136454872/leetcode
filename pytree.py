class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x=0, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def travel(self, order='pre'):
        # order : pre,mid,post

        if order != 'pre' and order != 'mid' and order != 'post':
            print('order error: ', order)
        self.travel_sub(order)
        print()

    def travel_sub(self, order):
        if order == 'pre':
            print(self.val, end=' ')

        if self.left is not None:
            self.left.travel_sub(order)

        if order == 'mid':
            print(self.val, end=' ')

        if self.right is not None:
            self.right.travel_sub(order)

        if order == 'post':
            print(self.val, end=' ')

    def searchNode(self, target):
        if self.val == target:
            return self

        if self.left is not None:
            t = self.left.searchNode(target)

            if t:
                return t

        if self.right is not None:
            t = self.right.searchNode(target)

            if t:
                return t

        return None

    @classmethod
    def fromStrList(self, s):
        null = None
        data = eval(s)

        if len(data) == 1 and data[0] is None:
            return None
        root = TreeNode(data[0])
        queue = [root]
        data.pop(0)

        while len(data) > 0:
            node = queue.pop(0)

            if len(data) > 0:
                left = data.pop(0)
            else:
                left = None

            if len(data) > 0:
                right = data.pop(0)
            else:
                right = None

            if left is not None:
                node.left = TreeNode(left)
                queue.append(node.left)

            if right is not None:
                node.right = TreeNode(right)
                queue.append(node.right)

        return root


if __name__ == '__main__':
    inp = '[7, 3, 15, null, null, 9, 20]'
    inp = '[1]'
    root = TreeNode.fromStrList(inp)
    root.travel("mid")
