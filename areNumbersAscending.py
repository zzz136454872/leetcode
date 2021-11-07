from typing import List


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split()
        pre = -1

        for token in s:
            if token[0].isdigit():
                token = int(token)
                print(token)

                if token <= pre:
                    return False
                pre = token

        return True


s = "hello world 5 x 5"
print(Solution().areNumbersAscending(s))
