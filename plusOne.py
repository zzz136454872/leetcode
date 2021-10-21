from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1

        while i >= 0 and digits[i] == 9:
            i -= 1

        for j in range(i + 1, len(digits)):
            digits[j] = 0

        if i >= 0:
            digits[i] += 1
        else:
            digits.insert(0, 1)

        return digits


digits = [1, 2, 3]
digits = [4, 3, 2, 1]
digits = [0]
digits = [1, 9]
print(Solution().plusOne(digits))
