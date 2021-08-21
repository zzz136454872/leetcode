from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        p1 = 0
        p2 = 0

        while p1 < len(chars):
            now = chars[p1]
            count = 0

            while p1 < len(chars) and chars[p1] == now:
                p1 += 1
                count += 1
            chars[p2] = now
            p2 += 1

            if count > 1:
                for letter in str(count):
                    chars[p2] = letter
                    p2 += 1
        # print(chars[:p2])

        return p2


sl = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
chars = ["a"]
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(sl.compress(chars))
