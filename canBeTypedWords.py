class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        bk=set(letter for letter in brokenLetters)
        out=0

        for word in text:
            cannot=False
            for letter in word:
                if letter in bk:
                    cannot=True
                    break
            if not cannot:
                out+=1
        return out

sl=Solution()
text = "hello world"
brokenLetters = "ad"
text = "leet code"
brokenLetters = "lt"
text = "leet code"
brokenLetters = "e"
print(sl.canBeTypedWords(text,brokenLetters))

