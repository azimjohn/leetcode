class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        number_of_zeros = 0
        
        # todo: use 2 pointers
        for index in range(len(nums)-1, -1, -1):
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
