class Solution:
    def twoSum(self, numbers, target):
        complements = {}

        for index, number in enumerate(numbers):
            complements[target - number] = index

        for index, number in enumerate(numbers):
            if number in complements and complements[number] != index:
                return [index, complements[number]]
