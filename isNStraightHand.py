from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        if len(hand) % groupSize != 0:
            return False
        hand.sort(reverse=True)
        n = len(hand) // groupSize

        for i in range(n):
            a = hand.pop() + 1

            for j in range(groupSize - 1):
                find = False

                for k in range(len(hand) - 1, -1, -1):
                    if hand[k] == a:
                        a += 1
                        find = True
                        del hand[k]

                        break

                    if hand[k] > a:
                        return False

                if not find:
                    return False

        return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
W = 3
hand = [1, 2, 3, 4, 5]
W = 4
print(Solution().isNStraightHand(hand, W))
