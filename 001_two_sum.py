class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        m = {}
        for idx, n in enumerate(nums):
            # print(f'n[{idx}] = {n}')

            complement = target - n
            if m.get(complement) is not None:
                return [idx, m.get(complement)]

            m[n] = idx

        raise Exception('soulution not found')


if __name__ == '__main__':
    nums = [2, 11, 7, 15]
    target = 9

    print(f'input: nums = {nums}, target = {target}')
    print(f'output: {Solution().twoSum(nums, target)}')
