from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        elems = list(permutations(range(1,n+1)))[k-1]
        elems = [str(elem) for elem in elems]
        return "".join(elems)
