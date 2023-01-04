# wa

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        left=0
        right=0
        live=0
        m=0
        al = 0
        ar = 0

        if len(s)%2!=0:
            return False
        for i in range(len(s)):
            if locked[i]=='0':
                live+=1
            elif s[i]=='(':
                left+=1
            else:
                right+=1
            if s[i]=='(':
                al+=1
            else:
                ar+=1
            minL=max(0,ar-al)
            m=max(m,minL)
            if live<minL:
                return False

        if left>right+live:
            return False
        maxR=live-m
        if m+left>maxR+right:
            return False

        print(left,right,m,maxR)
        print(len(s),live)
        return True

s = "))()))"
locked = "010100"
s = "()()"
locked = "0000"
s = ")"
locked = "0"


s =      "((((())()())(())((())(()())((())))))(((((((())(()))))("
locked = "001110011011010111100111011101111110000101001101001111"
print(Solution().canBeValid(s,locked))
        
        
            
                
            
        
