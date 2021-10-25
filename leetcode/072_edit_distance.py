class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]

        # base case if word2 is empty
        for i in range(len(word1)+1):
            cache[i][len(word2)] = len(word1) - i
        # base case if word1 is empty
        for j in range(len(word2)+1):
            cache[len(word1)][j] = len(word2) - j

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    cache[i][j] = min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1]) + 1

        return cache[0][0]


if __name__ == '__main__':
    # Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
    # You have the following three operations permitted on a word:
    # Insert a character
    # Delete a character
    # Replace a character

    word1 = "horse"
    word2 = "ros"

    solution = Solution()
    ans = solution.minDistance(word1, word2)

    assert ans == 3, f'ans={ans}'
