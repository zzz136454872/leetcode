from pytree import TreeNode


class Codec:
    def serialize(self, root):
        queue = [root]
        i = 0

        while i < len(queue):
            node = queue[i]
            i += 1

            if node != None:
                queue.append(node.left)
                queue.append(node.right)

        return str([node.val if node is not None else None for node in queue])

    def deserialize(self, data):
        data = eval(data)

        if len(data) == 1:
            return None
        root = TreeNode(data[0])
        queue = [root]

        for j in range(1, len(data), 2):
            node = queue[j // 2]
            left = data[j]
            right = data[j + 1]

            if left != None:
                node.left = TreeNode(left)
                queue.append(node.left)

            if right != None:
                node.right = TreeNode(right)
                queue.append(node.right)

        return root


# Your Codec object will be instantiated and called as such:
root = '[2,1,3]'
root = TreeNode.fromStrList(root)
codec = Codec()
print(codec.serialize(root))
root = codec.deserialize(codec.serialize(root))
TreeNode.travel(root)
