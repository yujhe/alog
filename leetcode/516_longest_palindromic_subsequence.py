class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for l in range(1, n+1):
            for i in range(0, n-l+1):
                j = i + l - 1
                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]


if __name__ == '__main__':
    # Given a string s, find the longest palindromic subsequence's length in s.
    # A subsequence is a sequence that can be derived from another sequence
    # by deleting some or no elements without changing the order of the remaining elements.

    s = "bbbab"

    solution = Solution()
    ans = solution.longestPalindromeSubseq(s)

    assert ans == 4, f'ans={ans}'
