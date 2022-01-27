class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentence = sentence.split()
        punct = ['!', '.', ',']
        out = 0

        for word in sentence:
            if word[-1] in punct:
                word = word[:-1]
            flag = False

            for letter in word:
                if letter in punct or letter.isdigit():
                    flag = True

            if flag:
                continue
            word = word.split('-')

            if len(word) == 1:
                out += 1

                continue

            if len(word) > 2:
                continue

            for part in word:
                if len(part) == 0:
                    flag = True

                    break

            if flag:
                continue
            out += 1

        return out


sentence = "cat and  dog"
sentence = "!this  1-s b8d!"
sentence = "alice and  bob are playing stone-game10"
sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
sentence = '!'
print(Solution().countValidWords(sentence))
