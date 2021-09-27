from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for idx, n in enumerate(nums):
            complement = target - n
            if m.get(complement) is not None:
                return [idx, m.get(complement)]

            m[n] = idx

        return None


if __name__ == '__main__':
    # given an array of integers,
    # find the index of elements that sum up to target
    nums = [2, 7, 11, 15]
    target = 9

    solution = Solution()
    ans = solution.twoSum(nums, target)

    assert set(ans) == set([0, 1]), f'ans={ans}'
