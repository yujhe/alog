class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = {}

        for i, c in enumerate(s):
            # skip the char that contains in the longest string
            if c in longest and longest[c] > i:
                continue

            cur = {}
            for j in range(i, len(s)):
                if s[j] in cur:
                    break
                cur[s[j]] = j

            if len(cur) > len(longest):
                longest = cur

        return len(longest)


if __name__ == '__main__':
    input = 'abcabcbb'

    print(f'input: {input}')
    print(f'output: {Solution().lengthOfLongestSubstring(input)}')
