class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # m[i][j] means the longest subsequence in s1[0:i], s2[0:j]
        m = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    m[i][j] = 1 + m[i-1][j-1]
                else:
                    m[i][j] = max(m[i-1][j], m[i][j-1])

        return m[-1][-1]


if __name__ == '__main__':
    # given two strings,
    # return the length of their longest common subsequence
    # a subsequence of a string generated from the original string with some characters (can be none)
    # For example, "ace" is a subsequence of "abcde".

    text1 = "abcde"
    text2 = "ace"

    solution = Solution()
    ans = solution.longestCommonSubsequence(text1, text2)

    assert ans == 3, f'ans={ans}'
