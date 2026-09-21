class Solution(object):
    def isMatch(self, s, p):
        m, n = len(s), len(p)

        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 2]

        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = False

            for j in range(1, n + 1):
                temp = dp[j]   

                if p[j - 1] == '*':
                  
                    dp[j] = dp[j - 2]

              
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[j] = dp[j] or temp

                else:
                   
                    dp[j] = prev and (
                        p[j - 1] == '.' or p[j - 1] == s[i - 1]
                    )

                prev = temp

        return dp[n]