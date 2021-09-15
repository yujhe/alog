from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for n in nums:
            sum += n

        n = len(nums)

        return int((1+n)*n/2 - sum)


if __name__ == '__main__':
    input = [3, 0, 1]

    print(f'input: {input}')
    print(f'output: {Solution().missingNumber(input)}')
