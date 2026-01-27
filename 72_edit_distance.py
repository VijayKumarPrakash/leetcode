class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = "*" + word1
        word2 = "*" + word2
        dp = [[i for i in range(len(word1))] for j in range(len(word2))]
        
        # Manually set first column
        for i in range(len(word2)):
            dp[i][0] = i

        for i in range(1, len(word2)):
            for j in range(1, len(word1)):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        return dp[len(dp)-1][len(dp[0])-1]
    

# Example usage:
sol = Solution()
print(sol.minDistance("horse", "ros"))  # Output: 3
print(sol.minDistance("intention", "execution"))  # Output: 5
print(sol.minDistance("hospital", "petal"))  # Output: 4
print(sol.minDistance("three", "eight"))  # Output: 5