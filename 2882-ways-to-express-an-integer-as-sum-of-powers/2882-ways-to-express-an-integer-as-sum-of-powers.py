class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        mod=10**9+7
        dp=[1]+[0]*n
        a=1
        while(power:=a**x)<=n:
            for i in range(n,power-1,-1):
                dp[i]=(dp[i]+dp[i-power])%mod
            a+=1
        return dp[n]