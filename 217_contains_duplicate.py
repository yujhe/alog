from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            if num in d:
                return True
            else:
                d[num] = num
        return False


if __name__ == '__main__':
    input = [1, 2, 3, 1]

    print(f'input: {input}')
    print(f'output: {Solution().containsDuplicate(input)}')
