from typing import List


# 768. 最多能完成排序的块 II
# 769. 最多能完成排序的块
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        def same(a, b):
            try:
                for k in a:
                    if a[k] != b[k]:
                        return False

                return True
            except:
                return False

        count = 0
        arr2 = arr.copy()
        arr2.sort()

        a = {}
        b = {}

        for i in range(len(arr)):
            a[arr[i]] = a.get(arr[i], 0) + 1
            b[arr2[i]] = b.get(arr2[i], 0) + 1

            if same(a, b):
                a = {}
                b = {}
                count += 1

        return count


arr = [5, 4, 3, 2, 1]
arr = [2, 1, 3, 4, 4]
print(Solution().maxChunksToSorted(arr))
