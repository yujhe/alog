from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > min_price:
                max_profit = max(max_profit, prices[i] - min_price)
            elif prices[i] < min_price:
                min_price = prices[i]

        return max_profit


if __name__ == '__main__':
    # given an array of stock prices in day n
    # return the max profit by buy and sell on different day

    prices = [7, 1, 5, 3, 6, 4]

    solution = Solution()

    assert solution.maxProfit(
        prices) == 5, f'max profit={solution.maxProfit(prices)}'
