from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        last = ''

        while len(bits) > 0:
            if bits[0] == 1:
                last = bits[:2]
                bits = bits[2:]
            else:
                last = bits[:1]
                bits = bits[1:]

        return last[0] == 0
