from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        lists = [ord(letter) for letter in s]
        lists.sort()
        n = len(lists)
        out = []

        while True:
            out.append(''.join([chr(i) for i in lists]))
            i = n - 1

            while i > 0 and lists[i] <= lists[i - 1]:
                i -= 1

            if i == 0:
                break
            i -= 1
            j = n - 1

            while lists[j] <= lists[i]:
                j -= 1
            lists[i], lists[j] = lists[j], lists[i]
            i += 1
            j = n - 1

            while i < j:
                lists[i], lists[j] = lists[j], lists[i]
                i += 1
                j -= 1

        return out


sl = Solution()
s = "bbc"
print(sl.permutation(s))
