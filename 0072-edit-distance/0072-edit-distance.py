class Solution(object):
    def minDistance(self, word1, word2):
        dp = list(range(len(word2) + 1))
        for i in range(1, len(word1) + 1):
            old = dp[0]
            dp[0] = i
            for j in range(1, len(word2) + 1):
                x = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = old
                else:
                    dp[j] = 1 + min(old, dp[j], dp[j-1])
                old = x

        return dp[-1]
        