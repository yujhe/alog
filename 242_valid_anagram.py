class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)


if __name__ == '__main__':
    # given two strings,
    # return true if the two string are anagram
    # anagram are strings that contains the same characters
    s = "anagram"
    t = "nagaram"

    solution = Solution()

    assert solution.isAnagram(s, t)
