from typing import *


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]],
                       needs: List[int]) -> int:
        self.bag = special
        self.price = price
        self.n = len(special)

        return self.shop(0, needs)

    def shop(self, choice, need):
        if choice == self.n:
            out = 0

            for i in range(len(self.price)):
                out += self.price[i] * need[i]

            return out
        maxCount = 123456

        for i in range(len(self.price)):
            if self.bag[choice][i] > 0:
                maxCount = min(maxCount, need[i] // self.bag[choice][i])
        out = 1234567

        for i in range(maxCount + 1):
            tmp = i * self.bag[choice][-1]
            newNeeds = [
                need[j] - i * self.bag[choice][j]
                for j in range(len(self.price))
            ]
            tmp += self.shop(choice + 1, newNeeds)
            out = min(out, tmp)

        return out


price, special, needs = [2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]
sl = Solution()
print(sl.shoppingOffers(price, special, needs))
