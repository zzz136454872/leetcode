from typing import List


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def long(letter):
            out = 0
            r = 0
            count = 0

            for l in range(len(answerKey)):
                while r < len(answerKey) and (count < k or count == k
                                              and answerKey[r] == letter):
                    if answerKey[r] != letter:
                        count += 1
                    r += 1
                out = max(out, r - l)

                if answerKey[l] != letter:
                    count -= 1

            return out

        return max(long('F'), long('T'))


answerKey = "TTFF"
k = 2
answerKey = "TFFT"
k = 1
answerKey = "TTFTTFTT"
k = 1
print(Solution().maxConsecutiveAnswers(answerKey, k))
