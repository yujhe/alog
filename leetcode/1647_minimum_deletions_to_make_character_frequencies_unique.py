from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        # get char frequency, ex: 'aabbc' -> [2, 2, 1]
        n = Counter(s).values()

        # decrease the number of frequency if the char is not good
        deletion = 0
        unique = set()

        for freq in n:
            while freq in unique:
                freq -= 1
                deletion += 1
            if freq > 0:
                unique.add(freq)

        return deletion


if __name__ == '__main__':
    # given a string,
    # return the minimum number of deletion to make the string good
    # a good string means no two different characters have the same frequency

    s = "aab"

    solution = Solution()

    assert solution.minDeletions(s) == 0
