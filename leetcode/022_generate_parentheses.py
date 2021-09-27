from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(n, n, ans, '')
        return ans

    def dfs(self, left_num, right_num, rs, string):
        # skip case that `(` is more than `)`
        if right_num < left_num:
            return
        if left_num == 0 and right_num == 0:
            rs.append(string)
            return
        if left_num > 0:
            self.dfs(left_num-1, right_num, rs, f'{string}(')
        if right_num > 0:
            self.dfs(left_num, right_num-1, rs, f'{string})')


if __name__ == '__main__':
    # given n parentheses,
    # return all combinations of well-formed parentheses

    n = 3
    expect = ["((()))", "(()())", "(())()", "()(())", "()()()"]

    solution = Solution()
    ans = solution.generateParenthesis(n)

    assert len(ans) == len(expect), f'# of output={len(ans)}'
    for i in ans:
        assert i in expect, f'{i} is not correct'
