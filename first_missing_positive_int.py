# https://leetcode.com/problems/first-missing-positive/

def min_positive_missing_int(numbers):
    numbers = [number for number in numbers if number > 0]
    if not numbers:
        return 1

    seen = set(numbers)
    min_num = min(numbers)

    if min_num > 1:
        return 1

    candidates = []
    for number in numbers:
        if (number + 1) not in seen:
            candidates.append(number+1)

    return min(candidates)


if __name__ == '__main__':
    cases = [
        ([1, 3, 1, 4, 6, 2], 5),
        ([1, 2, 3], 4),
        ([-3, -5], 1),
        ([1, 4, 100], 2),
        ([1000, 10001, 2000], 1)
    ]

    for case in cases:
        print("PASS" if min_positive_missing_int(case[0]) == case[1] else "FAIL")

