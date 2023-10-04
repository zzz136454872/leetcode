from typing import List

# 买卖股票的最佳时机
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100000000
        profit=0
        for price in prices:
            min_price=min(min_price,price)
            profit=max(profit,price-min_price)
        return profit

# 买卖股票的最佳时机II

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        preMin=100000
        last=100000
        out=0
        for i in range(len(prices)):
            if prices[i]>last:
                last=prices[i]
                continue
            out+=last-preMin
            last=prices[i]
            preMin=last
        out+=last-preMin
        return out

#买卖股票的最佳时机III
class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        k=2
        profit=[0 for i in range(k+1)]
        buy=[123456789 for i in range(k+1)]
        for p in prices:
            for i in range(1,k+1):
                buy[i]=min(buy[i],p-profit[i-1])
                profit[i]=max(profit[i],p-buy[i])
        return profit[-1]

#买卖股票的最佳时机IV
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k=min(k,len(prices)//2)
        profit=[0 for i in range(k+1)]
        buy=[123456789 for i in range(k+1)]
        for p in prices:
            for i in range(1,k+1):
                buy[i]=min(buy[i],p-profit[i-1])
                profit[i]=max(profit[i],p-buy[i])
        return profit[-1]

# 销售价值减少的颜色球
class Solution10:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        if orders==0:
            return 0
        inventory.sort(reverse=True)
        inventory.append(0)
        count=0
        for i in range(len(inventory)):
            count+=(i+1)*(inventory[i]-inventory[i+1])
            if count>=orders:
                height=inventory[i+1]
                more=count-orders
                columns=i+1
                break
        out=0
        more_height=more//columns
        height+=more_height
        more=more%columns
        # print(more,height)

        for c in inventory:
            if c<=height:
                break
            out+=(c+height+1)*(c-height)//2

        out-=more*(height+1)
        return out%(10**9+7)

# sl=Solution()
# prices=[7,1,5,3,6,4]
# print(sl.maxProfit(prices))

k = 2
prices = [3,2,6,5,0,3]
sl=Solution()
print(sl.maxProfit(k,prices))
            
