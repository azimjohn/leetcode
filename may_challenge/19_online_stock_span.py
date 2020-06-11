class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        ans = 1
        while self.prices and price >= self.prices[-1][0]:
            _, count = self.prices.pop()
            ans += count

        self.prices.append([price, ans])

        return ans
