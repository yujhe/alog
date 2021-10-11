from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # track char count
        t_counter, s_counter = Counter(t), Counter()
        t_chars = len(t_counter.keys())

        matches = 0  # matched chars
        min_substr = ''

        l, r = 0, -1
        while l < len(s):
            if matches < t_chars:
                # move right pointer
                r += 1

                if r == len(s):
                    break

                c = s[r]
                s_counter[c] += 1
                if c in t_counter and s_counter[c] == t_counter[c]:
                    matches += 1
            else:
                # move left pointer
                c = s[l]
                s_counter[c] -= 1
                if c in t_counter and s_counter[c] == t_counter[c]-1:
                    matches -= 1
                l += 1

            if matches == t_chars:
                if not min_substr or r-l+1 < len(min_substr):
                    min_substr = s[l:r+1]

        return min_substr


if __name__ == '__main__':
    # given two strings s and t
    # return the minimum window substring of s such that every character in t is included in the window
    # return the empty string "" if no such substring

    s = "aa"
    t = "aa"

    solution = Solution()
    ans = solution.minWindow(s, t)

    assert ans == 'aa', f'ans={ans}'
