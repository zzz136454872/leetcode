class Solution:
    def minLength(self, s: str) -> int:
        r = []

        for letter in s:
            if letter == 'B':
                if len(r) > 0 and r[-1] == 'A':
                    r.pop()
                else:
                    r.append(letter)
            elif letter == 'D':
                if len(r) > 0 and r[-1] == 'C':
                    r.pop()
                else:
                    r.append(letter)
            else:
                r.append(letter)

        return len(r)


s = "ABFCACDB"
s = 'ACBBD'
print(Solution().minLength(s))
