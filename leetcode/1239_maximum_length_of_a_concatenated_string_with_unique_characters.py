from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        unique = ['']

        for s in arr:
            for u in unique:
                concat = s + u
                if len(concat) == len(set(concat)):
                    unique.append(concat)
                    max_len = max(max_len, len(concat))

        return max_len


if __name__ == '__main__':
    # given an array of strings,
    # return the maximum concatenation length by strings in the array
    # the characters in the concatenation should be unique
    #
    # Input: arr = ["un","iq","ue"]
    # Output: 4
    # Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
    # Maximum length is 4.

    arr = ["cha", "r", "act", "ers"]

    solution = Solution()
    ans = solution.maxLength(arr)

    assert ans == 6, f'ans={ans}'
