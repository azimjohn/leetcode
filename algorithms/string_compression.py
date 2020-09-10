class Solution:
    def compress(self, chars: List[str]) -> int:
        prev = chars[0]
        i = count = 0

        for char in chars:
            if char == prev:
                count += 1
                continue

            chars[i] = prev
            i += 1

            if count != 1:
                for digit in str(count):
                    chars[i] = digit
                    i += 1

            count = 1
            prev = char

        chars[i] = prev
        i += 1
        if count != 1:
            for digit in str(count):
                chars[i] = digit
                i += 1

        return i
