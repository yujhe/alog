from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1

        bucket = [None] * (len(nums) + 1)
        for num, count in m.items():
            if bucket[count]:
                bucket[count].append(num)
            else:
                bucket[count] = [num]

        ans = []
        i = len(bucket) - 1
        while i >= 0:
            if bucket[i]:
                ans = ans + bucket[i]
            if len(ans) == k:
                break
            i -= 1

        return ans


if __name__ == '__main__':
    input = [1, 2]
    k = 2

    print(f'input: {input}, k: {k}')
    print(f'output: {Solution().topKFrequent(input, k)}')
