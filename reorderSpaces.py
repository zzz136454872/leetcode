from typing import List


class Solution:
    def reorderSpaces(self, text: str) -> str:
        s = text.count(' ')
        text = text.split()
        n = len(text)

        if n > 1:
            k = s // (n - 1)
            r = s % (n - 1)
        else:
            k = 0
            r = s
        res = (' ' * k).join(text)

        return res + r * ' '


text = "  this   is  a sentence "
text = " practice   makes   perfect"
print(Solution().reorderSpaces(text), 'a', sep='')
