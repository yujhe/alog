from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # use dfs to iterate all possible solution
        ans = []
        self.dfs(candidates, target, [], ans)

        return ans

    def dfs(self, nums, target, path, ans):
        if target < 0:
            return
        if target == 0:
            ans.append(path)
            return
        for idx, n in enumerate(nums):
            self.dfs(nums[idx:], target-n, path+[n], ans)


if __name__ == '__main__':
    # given an array of distinct integers,
    # return all possible solutions that sum up to target
    # the same number could be chosen in unlimited time
    #
    # Input: candidates = [2,3,6,7], target = 7
    # Output: [[2,2,3],[7]]
    # Explanation:
    # 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
    # 7 is a candidate, and 7 = 7.
    # These are the only two combinations.

    input = [2, 3, 6, 7]
    output = [[2, 2, 3], [7]]
    target = 7

    solution = Solution()
    ans = solution.combinationSum(input, target)

    assert len(ans) == len(output), f'# of answer={len(ans)}'
    for i in ans:
        assert i in output, f'answer {i} is not correct'
