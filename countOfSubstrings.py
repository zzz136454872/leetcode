from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        t = k + 5
        m = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        res = 0

        def check():
            nonlocal mem, r

            if r > k:
                return 1
            elif r < k:
                return -1

            for i in range(5):
                if mem[i] < 1:
                    return -1

            return 0

        def add(letter):
            nonlocal mem, r

            if letter in m:
                mem[m[letter]] += 1
            else:
                r += 1

        for i in range(len(word) - t + 1):
            mem = [0] * 5
            r = 0

            for j in range(t):
                add(word[i + j])
            tmp = check()

            if tmp == 0:
                res += 1

            for j in range(t, len(word) - i):
                add(word[i + j])
                tmp = check()

                if tmp == 0:
                    res += 1
                elif tmp > 0:
                    break

        return res


word = "aeioqq"
k = 1
word = "aeiou"
k = 0
word = "ieaouqqieaouqq"
k = 1
# word = "iqeaouqi"
# k=2
print(Solution().countOfSubstrings(word, k))
