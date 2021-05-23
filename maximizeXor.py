from typing import List


class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None


class Solution:
    def maximizeXor(self, nums: List[int],
                    queries: List[List[int]]) -> List[int]:
        def n2s(n):
            n = bin(n)[2:]

            return '0' * (32 - len(n)) + n

        root = TreeNode()
        nums.sort()

        for i, query in enumerate(queries):
            query.append(i)
        queries.sort(key=lambda x: x[1])
        midTable = []
        loc = 0

        for query in queries:
            # print(query)

            while loc < len(nums) and nums[loc] <= query[1]:
                tmp = root
                numStr = n2s(nums[loc])
                # print('inside',nums[loc])
                loc += 1

                for b in numStr:
                    if b == '0':
                        if tmp.left is None:
                            tmp.left = TreeNode()
                        tmp = tmp.left
                    else:
                        if tmp.right is None:
                            tmp.right = TreeNode()
                        tmp = tmp.right

            if loc == 0:
                midTable.append([query[2], -1])

                continue

            numStr = n2s(query[0])
            # print('numStr',numStr)
            mXor = 0
            tmp = root

            for i in range(32):
                # if i==30:
                #     print('now')
                #     print(tmp)

                if numStr[i] == '0':
                    if tmp.right is not None:
                        tmp = tmp.right
                        mXor += 1 << (31 - i)
                    else:
                        tmp = tmp.left
                else:
                    if tmp.left is not None:
                        tmp = tmp.left
                        mXor += 1 << (31 - i)
                    else:
                        tmp = tmp.right

            # print('mXor',mXor)

            midTable.append([query[2], mXor])
        midTable.sort()

        return [item[1] for item in midTable]


nums = [5, 2, 4, 6, 6, 3]
queries = [[12, 4], [8, 1], [6, 3]]
sl = Solution()
print(sl.maximizeXor(nums, queries))
