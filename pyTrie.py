class Trie:
    def __init__(self):
        self.has = False
        self.sons = [None for i in range(26)]
