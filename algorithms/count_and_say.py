def count_and_say(num):
    say = ""
    count = 1
    prev = num[0]
    
    for digit in num[1:]:
        if digit == prev:
            count += 1
            continue
        say += str(count) + prev
        prev = digit
        count = 1

    return say + str(count) + prev 

if __name__ == '__main__':
    cases = [
        ["1", "11"],
        ["11", "21"],
        ["21", "1211"],
        ["1211", "111221"],
        ["111221","312211"]
    ]

    for case in cases:
        print("PASS" if count_and_say(case[0]) == case[1] else "FAIL")
