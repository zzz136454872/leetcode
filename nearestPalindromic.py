

# wrong answer

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        def isPali(n):
            return n==n[::-1]
        l=len(sn)
        if l%2==0:
            flag=0
            mid=sn[:l//2]# +sn[:l//2][::-1]
        else:
            flag=1
            mid=sn[:(l+1)//2]# +sn[:l//2][::-1]


sl=Solution()
inp=[1,10,11,100]
for i in inp:
    print(i,sl.nearestPalindromic(i))
