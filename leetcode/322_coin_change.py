from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if coins=[1, 2, 5] and amount=11
        # we can use bottom-up solution to find the mininum number of coins that sum up equals amount
        # dp[0] = 0 (for amount=0, the min number of coins = 0)
        # dp[1] = 1 (for amount=1, the min number of coins = 1)
        # ...
        # dp[3] = min(1+dp[3-1], 1+dp[3-1]) (for amount=3, we can take 1 coin or 2 coin than solve the sub-problem)

        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])

        return -1 if dp[amount] > amount else dp[amount]


if __name__ == '__main__':
    # given conins and a integer value
    # return the minimum number of coins that sum up to the value
    # you can take any number of coins

    coins = [1, 2, 5]
    amount = 11

    solution = Solution()
    ans = solution.coinChange(coins, amount)

    assert ans == 3, f'ans={ans}'
