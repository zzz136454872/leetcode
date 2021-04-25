class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    @classmethod
    def fromStrList(self, s):
        null = None
        data = eval(s)

        if len(data) == 1:
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
    root = TreeNode.fromStrList(inp)
    root.travel("mid")
