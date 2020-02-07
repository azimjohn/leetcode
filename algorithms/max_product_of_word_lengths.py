class Solution:
    word_mask = {}

    def maxProduct(self, words: List[str]) -> int:
        self.word_mask = {word: self.mask(word) for word in words}
        global_max = 0

        for word_one, mask_one in self.word_mask.items():
            for word_two, mask_two in self.word_mask.items():
                if self.isValid(mask_one, mask_two):
                    global_max = max(global_max, len(word_one) * len(word_two))

        return global_max

    def isValid(self, mask_one, mask_two):
        return mask_one & mask_two == 0

    def mask(word: str) -> int:
        return
