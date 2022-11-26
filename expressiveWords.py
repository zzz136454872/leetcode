from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def count(a):
            out = []
            prev = ''
            cnt = 0

            for i in range(len(a)):
                if a[i] == prev:
                    cnt += 1
                else:
                    out.append((prev, cnt))
                    cnt = 1
                    prev = a[i]
            out.append((prev, cnt))

            return out[1:]

        s = count(s)
        n = len(s)
        res = 0

        for word in words:
            w = count(word)

            if n != len(w):
                continue
            able = True

            for i in range(n):
                if w[i][0] != s[i][0] or w[i][1] > s[i][
                        1] or w[i][1] < s[i][1] and s[i][1] < 3:
                    able = False

                    break

            if able:
                res += 1

        return res


s = "heeellooo"
words = ["hello", "hi", "helo"]
print(Solution().expressiveWords(s, words))
