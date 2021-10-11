class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        for i in range(len(sentence)):
            if sentence[i][0] in vowels:
                sentence[i] = sentence[i] + 'ma' + (i + 1) * 'a'
            else:
                sentence[i] = sentence[i][1:] + sentence[i][0] + 'ma' + (
                    i + 1) * 'a'

        return ' '.join(sentence)


sentence = "I speak Goat Latin"
print(Solution().toGoatLatin(sentence))
