class Solution:
    def checkInclusion(self, p: str, s: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        if p_len > s_len:
            return False

        p_counter = collections.Counter(p)
        s_counter = collections.Counter(s[:p_len])

        if p_counter == s_counter:
            return True

        for i in range(p_len, s_len):
            start, end = s[i-p_len], s[i]

            s_counter[end] += 1
            s_counter[start] -= 1

            if not s_counter[start]:
                del s_counter[start]

            if s_counter == p_counter:
                return True

        return False
