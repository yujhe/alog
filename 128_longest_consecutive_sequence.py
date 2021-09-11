class UnionFindSolution:
    def longestConsecutive(self, nums) -> int:
        n = len(nums)

        if n == 0:
            return

        # initial parent and size
        parent = [i for i in range(n)]
        size = [1] * n

        def find(p):
            while (p != parent[p]):
                parent[p] = parent[parent[p]]
                p = parent[p]

            return p

        def union(p, q):
            global max_size

            root_p = find(p)
            root_q = find(q)

            if root_p == root_q:
                return

            if size[root_p] < size[root_q]:
                parent[root_p] = root_q
                size[root_q] += size[root_p]
            else:
                parent[root_q] = parent[root_p]
                size[root_p] += size[root_q]
            return

        m = {}
        for idx, n in enumerate(nums):
            if m.get(n) is not None:
                continue

            # union with the consecutive number
            if m.get(n-1) is not None:
                union(idx, m.get(n-1))
            if m.get(n+1) is not None:
                union(idx, m.get(n+1))

            m[n] = idx

        return max(size)


class SetSolution:
    def longestConsecutive(self, nums) -> int:
        longest = 0
        nums = set(nums)

        for n in nums:
            # skip the number we have scan before
            if n - 1 in nums:
                continue

            count = 1
            while n + 1 in nums:
                n += 1
                count += 1

            longest = count if count > longest else longest

        return longest


if __name__ == '__main__':
    nums = [1, 2, 0, 1]

    print(f'input: {nums}')
    print(
        f'output (UFSolution): {UnionFindSolution().longestConsecutive(nums)}')

    print(f'input: {nums}')
    print(f'output (SetSolution): {SetSolution().longestConsecutive(nums)}')
