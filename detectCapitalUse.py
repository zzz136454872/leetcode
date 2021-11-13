class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allUp = False
        firstUp = False

        if len(word) < 2:
            return True

        if word[0].isupper():
            firstUp = True

        if word[1].isupper():
            if not firstUp:
                return False
            allUp = True

        for letter in word[2:]:
            if letter.isupper():
                if not allUp:
                    return False

            if letter.islower():
                if allUp:
                    return False

        return True


word = "USA"
word = "FlaG"
print(Solution().detectCapitalUse(word))
