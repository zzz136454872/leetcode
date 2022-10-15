from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        j = 1

        for num in target:
            while num != j:
                res.append('Push')
                res.append('Pop')
                j += 1
            res.append('Push')
            j = num + 1

        return res


target = [1, 3]
n = 3
print(Solution().buildArray(target, n))
