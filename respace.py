from typing import *

def get_ord(letter):
    return ord(letter)-ord('a')

class Trie:
    def __init__(self):
        self.next=[None for i in range(26)]
        self.have=False

    def is_end(self):
        for poss in self.next:
            if poss!=None:
                return False
        return True
        
class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        root=Trie()
        for word in dictionary:
            tmp=root
            for i in range(len(word)-1,-1,-1):
                num=get_ord(word[i])
                if tmp.next[num]==None:
                    tmp.next[num]=Trie()
                tmp=tmp.next[num]
            tmp.have=True
        log=[i for i in range(len(sentence)+1)]
        for i in range(1,len(sentence)+1):
            tmp=root
            for j in range(i-1,-1,-1):
                log[i]=min(log[i],log[j]+i-j)
                if tmp.next[get_ord(sentence[j])]!=None:
                    tmp=tmp.next[get_ord(sentence[j])]
                    if tmp.have:
                        log[i]=min(log[i],log[j])
                else:
                    break
        print(log)
        return log[-1]
sl=Solution()
dictionary = ["looked","just","like","her","brother"]
sentence = "jesslookedjustliketimherbrother"
#dictionary=['i','am','boy']
#sentence='iamaboy'
print(sl.respace(dictionary,sentence))

        

