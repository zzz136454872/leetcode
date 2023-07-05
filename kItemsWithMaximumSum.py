class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int,
                             numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        k -= numOnes

        if k <= numZeros:
            return numOnes
        k -= numZeros

        return numOnes - k


numOnes = 3
numZeros = 2
numNegOnes = 0
k = 2
numOnes = 3
numZeros = 2
numNegOnes = 0
k = 4
numOnes = 3
numZeros = 3
numNegOnes = 5
k = 11
print(Solution().kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))
