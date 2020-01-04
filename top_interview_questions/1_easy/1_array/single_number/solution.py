# https://leetcode.com/problems/single-number/submissions/


def single_number(nums):
    xor_sum = 0

    for num in nums:
        xor_sum = xor_sum ^ num

    return xor_sum


if __name__ == '__main__':
    cases = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4)
    ]

    for case in cases:
        assert single_number(case[0]) == case[1]
