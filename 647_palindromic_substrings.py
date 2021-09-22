class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        # expand around of the center string
        # the center string could be 1 or 2 letters, ex: aba, abba
        for i in range(len(s)):
            count += self.expand(s, i, i)
            count += self.expand(s, i, i+1)

        return count

    def expand(self, s, left, right) -> int:
        count = 0
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            else:
                break

        return count


if __name__ == '__main__':
    # given a string,
    # retun the # of palindromic substrings (string is palindrome when it reads the same backward as forward)
    s = 'aaa'
    solution = Solution()

    assert solution.countSubstrings(
        s) == 6, f'solution.countSubstrings(s)={solution.countSubstrings(s)}'
