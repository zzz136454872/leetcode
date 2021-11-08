from typing import List


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b = 0
        c = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
        map1 = [0 for i in range(10)]
        map2 = [0 for i in range(10)]

        for num in secret:
            map1[int(num)] += 1

        for num in guess:
            map2[int(num)] += 1

        for i in range(10):
            c += min(map1[i], map2[i])

        return str(b) + 'A' + str(c - b) + 'B'


secret = "1807"
guess = "7810"
secret = "1123"
guess = "0111"
secret = "1"
guess = "0"
print(Solution().getHint(secret, guess))
