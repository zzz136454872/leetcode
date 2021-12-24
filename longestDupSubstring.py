class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)

        def exists(length):
            mem = {}

            for i in range(n - length + 1):
                sub = s[i:i + length]
                h = hash(sub)

                if h in mem:
                    for idx in mem[h]:
                        if s[idx:idx + length] == s[i:i + length]:
                            return idx
                    s[h].append(i)
                else:
                    mem[h] = [i]

            return -1

        left = 0
        right = n - 1
        l = -1

        while left <= right:
            mid = (left + right) // 2
            tmp = exists(mid)

            if tmp != -1:
                l = tmp
                left = mid + 1
            else:
                right = mid - 1

        return s[l:l + left - 1]


s = "banana"
s = "abcd"
s = "nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy"
print(Solution().longestDupSubstring(s))
