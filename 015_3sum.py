from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx-1]:
                continue

            # 2 sum problem, find value a + b = -n
            m = {}
            for i in range(idx+1, len(nums)):
                if i+1 < len(nums) and nums[i] == nums[i+1]:
                    m[nums[i]] = i
                    continue

                complement = -n - nums[i]
                if complement in m:
                    ans.append([n, nums[i], complement])

                m[nums[i]] = i

        return ans


if __name__ == '__main__':
    input = [0, 0, 0, 0]

    print(f'input: {input}')
    print(f'output: {Solution().threeSum(input)}')
