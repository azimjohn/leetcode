class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)

        if p_len > s_len:
            return []

        p_counter = collections.Counter(p)
        s_counter = collections.Counter(s[:p_len])
        result = []

        if p_counter == s_counter:
            result.append(0)

        for i in range(p_len, s_len):
            start, end = s[i-p_len], s[i]

            s_counter[end] += 1
            s_counter[start] -= 1

            if not s_counter[start]:
                del s_counter[start]

            if s_counter == p_counter:
                result.append(i-p_len+1)

        return result
