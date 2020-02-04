class Solution:
    """ Complexity: len(word) * (len(words) ** 2), todo: it could be better """
    wordset = None

    def maxProduct(self, words: List[str]) -> int:
        self.wordset = [set(word) for word in words]
        global_max = 0

        for index_one, word_one in enumerate(words):
            for index_two, word_two in enumerate(words):
                if self.isValid(index_one, index_two):
                    global_max = max(global_max, len(word_one) * len(word_two))

        return global_max

    def isValid(self, index_one, index_two):
        wordset_one = self.wordset[index_one]
        wordset_two = self.wordset[index_two]

        return not bool(wordset_one.intersection(wordset_two))
