from collections import defaultdict


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mem = defaultdict(int)

        for letter in text:
            mem[letter] += 1
        out = 12345
        out = min(out, mem['b'])
        out = min(out, mem['a'])
        out = min(out, mem['l'] // 2)
        out = min(out, mem['o'] // 2)
        out = min(out, mem['n'])

        return out


text = "nlaebolko"
text = "leetcode"
text = "loonbalxballpoon"
print(Solution().maxNumberOfBalloons(text))
