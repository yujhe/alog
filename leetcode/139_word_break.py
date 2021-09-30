from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # if s[i:j] == words in dictionary
        # then s[:j] can be segmented only when s[:i-1] can be segmented

        segmented = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                if s[i-len(word)+1:i+1] == word:
                    if i == len(word) - 1:
                        segmented[i] = True
                    else:
                        segmented[i] |= segmented[i-len(word)]

        return segmented[-1]


if __name__ == '__main__':
    # given a string and a dictionary of strings,
    # return true if the string can be segmented into a words in dictionary
    #
    # Input: s = "leetcode", wordDict = ["leet","code"]
    # Output: true
    # Explanation: Return true because "leetcode" can be segmented as "leet code".

    s = "leetcode"
    wordDict = ["leet", "code"]

    soltion = Solution()
    ans = soltion.wordBreak(s, wordDict)

    assert ans == True
