class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def pair(s1, s2):
            i = 0
            j = len(s1) - 1

            while i < j and s1[i] == s2[j]:
                i += 1
                j -= 1

            if i >= j:
                return True
            i1 = i
            j1 = j

            while i1 < j1 and s1[i1] == s1[j1]:
                i1 += 1
                j1 -= 1

            if i1 >= j1:
                return True
            i1 = i
            j1 = j

            while i1 < j1 and s2[i1] == s2[j1]:
                i1 += 1
                j1 -= 1

            if i1 >= j1:
                return True

            return False

        return pair(a, b) or pair(b, a)


a = "x"
b = "y"
a = "abdef"
b = "fecab"
a = "ulacfd"
b = "jizalu"
a = "abda"
b = "acmc"
print(Solution().checkPalindromeFormation(a, b))
