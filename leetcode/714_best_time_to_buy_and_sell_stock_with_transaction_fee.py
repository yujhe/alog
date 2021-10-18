from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # the profit of your account in day[0]
        has_stock, no_stock = -prices[0], 0

        for price in prices[1:]:
            # update max profit if you sell stock
            no_stock = max(no_stock, has_stock + price - fee)
            # update max profit if you buy stock
            has_stock = max(has_stock, no_stock - price)

        return no_stock


if __name__ == '__main__':
    # given an array prices where prices[i] is the price of a given stock on the ith day,
    # and an integer fee representing a transaction fee.
    # return the maximum profit you can achieve

    prices = [1, 3, 2, 8, 4, 9]
    fee = 2

    solution = Solution()
    ans = solution.maxProfit(prices, fee)

    assert ans == 8, f'ans={ans}'
