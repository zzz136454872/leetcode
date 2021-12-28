def l2n(a):
    return ord(a) - ord('a')


class Trie:
    def __init__(self):
        self.has = False
        self.sons = [None for i in range(26)]

    def add(self, word):
        p = self

        for letter in word:
            idx = l2n(letter)

            if p.sons[idx] is None:
                p.sons[idx] = Trie()
            p = p.sons[idx]
        p.has = True
