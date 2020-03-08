
class Solution:
    def __init__(self):
        self.dic=dict()
       
    def coinChange(self, coins, amount) -> int:
        self.coins=coins
        return self.find(amount)
    
    def find(self,amount):
        if amount==0:
            return 0
        if amount<0:
            return 1000000
        if amount in self.dic.keys():
            return self.dic[amount]
        count=1000000
        for num in coins:
            tmp=self.find(amount-num)
            if tmp==-1:
                continue
            count=min(count,tmp+1)
        self.dic[amount]=count
        return count

sl=Solution()
coins=[1,2,5]
amount=11
out=sl.coinChange(coins,amount)
print(out)
