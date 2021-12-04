class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        def l2n(a):
            return ord(a) - ord('a')

        mem1 = [0] * 26
        mem2 = [0] * 26

        for letter in ransomNote:
            mem1[l2n(letter)] += 1

        for letter in magazine:
            mem2[l2n(letter)] += 1

        for i in range(26):
            if mem2[i] < mem1[i]:
                return False

        return True


ransomNote = "aa"
magazine = "ab"
print(Solution().canConstruct(ransomNote, magazine))
