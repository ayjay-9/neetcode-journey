class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0

        max_profit = 0
        buy_index, min_buy = 0, 0
        sell_index = buy_index + 1
        buy_pointer, sell_pointer = prices[buy_index], prices[sell_index]

        for i in range(len(prices) - 1):
            profit = sell_pointer - buy_pointer
            if profit > max_profit:
                max_profit = profit

            if sell_pointer < buy_pointer:  # -ve profit
                min_buy = sell_index
                if prices[min_buy] < prices[buy_index]:
                    buy_index = sell_index
                else:
                    buy_index += 1

                if sell_index != len(prices) - 1:
                    sell_index = buy_index + 1
                sell_pointer, buy_pointer = prices[sell_index], prices[buy_index]
            else:  # +ve profit
                if sell_index != len(prices) - 1:
                    sell_index += 1
                    sell_pointer = prices[sell_index]
        return max_profit

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([5,1,5,6,7,1]))