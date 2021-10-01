class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''

        # expand from the center, the center may be 1 or 2 characters
        for i in range(len(s)):
            sub1 = self.expand(s, i, i)
            sub2 = self.expand(s, i, i+1)

            sub = sub1 if len(sub1) > len(sub2) else sub2
            if len(sub) > len(longest):
                longest = sub

        return longest

    def expand(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break

        return s[left+1:right]


if __name__ == '__main__':
    # given a string,
    # return the longest palindromic substring in a

    s = 'babad'

    solution = Solution()
    ans = solution.longestPalindrome(s)

    assert ans == 'bab', f'ans={ans}'
