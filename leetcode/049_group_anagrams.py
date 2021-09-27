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

        return list(ans.values())


if __name__ == '__main__':
    # given an array of strings,
    # group the strings by anagrams, you can return it in any order
    # anagrams is formed by rearranging the letters, all the original letters exactly once.
    # ex: ['eat', 'ate', 'aet'] are anagrams

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']]

    solution = Solution()
    ans = solution.groupAnagrams(strs)

    assert len(ans) == len(output), f'# of ans={len(ans)}'
    for i in ans:
        i.sort()
        assert i in output, f'ans={i} is not correct'
