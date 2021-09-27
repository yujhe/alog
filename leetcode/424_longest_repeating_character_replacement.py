class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # iterate string with a window: i, j
        # in that window: len(substring) - max(duplicate chars) should <= k
        longest = 0
        chars_num = {}

        i = 0
        for j, c in enumerate(s):
            # update chars num of the substring
            chars_num[c] = chars_num.get(c, 0) + 1

            # resize the window if the replacement more than k times
            while (j - i + 1) - max(chars_num.values()) > k:
                chars_num[s[i]] -= 1
                i += 1

            longest = max(longest, j - i + 1)

        return longest


if __name__ == '__main__':
    # given a string and an integer k
    # you can replace characters of the string to any at most k times
    # return the # of longest repeating characters
    #
    # Input: s = "ABAB", k = 2
    # Output: 4
    # Explanation: Replace the two 'A's with two 'B's or vice versa.

    s = "ABBB"
    k = 2

    solution = Solution()
    ans = solution.characterReplacement(s, k)

    assert ans == 4, f'ans={ans}'
