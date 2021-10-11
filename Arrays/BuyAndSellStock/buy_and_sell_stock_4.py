
def maxProfit(prices, k):
    n=len(prices)
    dp=[0]*n
    max_profit=0
    
    if(k > n/2):
        for i in range(1,n):
            if(prices[i] > prices[i-1]):
                max_profit += (prices[i]-prices[i-1])
        return max_profit
       
    for p in range(k):
        pos -= prices[0]
        max_profit = 0
        
        for i in range(n):
            pos = max(pos, (dp[i]-prices[i]))
            max_profit = max(max_profit, (prices[i]+pos))
            dp[i] = max_profit
    
    return (dp[-1])

arr = []
k = int(input("Enter the number of allowed transactions : "))
n = int(input("Enter the number of elements in the array : "))

for i in range(0, n):
  element = int(input())
  arr.append(element) 

output = maxProfit(arr, k)
print(output)