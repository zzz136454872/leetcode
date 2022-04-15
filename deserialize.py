# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        pass

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        pass

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        pass

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        pass

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        pass


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = [NestedInteger()]
        tmp = -1
        flag = 1

        for letter in s:
            # print(letter)

            if letter.isdigit():
                if tmp != -1:
                    tmp = tmp * 10 + int(letter)
                else:
                    tmp = int(letter)
            else:
                if tmp != -1:
                    node = NestedInteger(flag * tmp)
                    tmp = -1
                    flag = 1
                    stack[-1].add(node)
                    # print(node.getInteger())

                if letter == '[':
                    stack.append(NestedInteger())
                elif letter == '-':
                    flag = -1
                elif letter == ']':
                    node = stack.pop()
                    stack[-1].add(node)

        if tmp != -1:
            node = NestedInteger(flag * tmp)
            tmp = -1
            flag = 1
            stack[-1].add(node)
            print(node.getInteger())

        return stack[-1].getList()[0]


s = "[123,[456,[789]]]"
print(Solution().deserialize(s))
