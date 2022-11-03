class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        l = 1
        r = len(sequence) // len(word)

        while l <= r:
            mid = (l + r) // 2
            w = mid * word

            if w in sequence:
                l = mid + 1
            else:
                r = mid - 1

        return l - 1
