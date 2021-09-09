from typing import *


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tmp = []
        tmplen = 0
        out = []

        for word in words:
            if len(tmp) == 0:
                tmp.append(word)
                tmplen += len(word)

                continue

            if tmplen + len(word) + 1 <= maxWidth:
                tmp.append(word)
                tmplen += len(word) + 1

                continue

            if len(tmp) > 1:
                rest = maxWidth - tmplen
                avg = rest // (len(tmp) - 1)
                buf = [1 + avg for i in range(len(tmp) - 1)]
                r = rest - (len(tmp) - 1) * avg

                for i in range(r):
                    buf[i] += 1
                tmpout = ''

                for i in range(len(tmp) - 1):
                    tmpout += tmp[i] + buf[i] * ' '
                tmpout += tmp[-1]
                out.append(tmpout)
            else:
                out.append(tmp[0] + (maxWidth - len(tmp[0])) * ' ')
            tmp = [word]
            tmplen = len(word)

        if len(tmp) > 0:
            tmpout = ''

            for word in tmp:
                if len(tmpout) > 0:
                    tmpout += ' '
                tmpout += word
            tmpout += (maxWidth - len(tmpout)) * ' '
            out.append(tmpout)

        return out


words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["What", "must", "be", "acknowledgment", "shall", "be"]
words = [
    "Science", "is", "what", "we", "understand", "well", "enough", "to",
    "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we",
    "do"
]

maxWidth = 16
maxWidth = 20
sl = Solution()
print(sl.fullJustify(words, maxWidth))
