from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] if n % 2 == 1 else []

        for i in range(n//2):
            ans = ans + [i+1, -(i+1)]

        return ans


if __name__ == '__main__':
    # given an integer n,
    # return any array containing n unique integers that add up to 0

    # Input: n = 5
    # Output: [-7,-1,1,3,4]
    # Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

    solution = Solution()

    assert sum(solution.sumZero(1)) == 0
    assert sum(solution.sumZero(2)) == 0
    assert sum(solution.sumZero(5)) == 0
