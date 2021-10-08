class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        chars = {}
        l = 0

        for r, c in enumerate(s):
            if c in chars:
                # char repeated, update the left index
                # `abcba`: 1) `b` repeated, l=chars['b']+1 2) `a` repeated, l=max(l, chars['a']+1)
                l = max(l, chars[c]+1)
            chars[c] = r
            longest = max(longest, r-l+1)

        return longest


if __name__ == '__main__':
    s = "abcabcbb"

    solution = Solution()
    ans = solution.lengthOfLongestSubstring(s)

    assert ans == 3, f'ans={ans}'
