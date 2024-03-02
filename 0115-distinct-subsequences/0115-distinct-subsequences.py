class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            dp[0][i] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) if s[i - 1] == t[j - 1] else dp[i - 1][j]
        return dp[n][m]