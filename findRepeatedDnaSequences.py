from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mem = set()
        out = set()

        for i in range(len(s) - 9):
            tmp = s[i:i + 10]

            if tmp in mem:
                out.add(tmp)
            else:
                mem.add(tmp)

        return list(out)


sl = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAAAA"
s = "AAAAAAAAAAA"
print(sl.findRepeatedDnaSequences(s))
