from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for str in strs:
            s_char = ''.join(sorted(str))

            if s_char in ans:
                ans[s_char].append(str)
            else:
                ans[s_char] = [str]

        return ans.values()


if __name__ == '__main__':
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(f'input: {input}')
    print(f'output: {Solution().groupAnagrams(input)}')
