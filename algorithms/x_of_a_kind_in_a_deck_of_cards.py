from functools import reduce


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = collections.Counter(deck)

        cards = list(counter.values())
        if len(cards) == 0:
            return False

        return reduce(math.gcd, cards) > 1
        