class Solution:
    def RabinKarp(self,text, M, q):
        if M == 0: return True
        h, t, d = (1 << (8 * M-8)) % q, 0, 256

        dict_ = defaultdict(list)

        for i in range(M): 
            t = (d * t + ord(text[i])) % q

        dict_[t].append(i-M+1)

        for i in range(len(text) - M):
            t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
            for j in dict_[t]:
                if text[i+1:i+M+1] == text[j:j+M]:
                    return (True, text[j:j+M])
            dict_[t].append(i+1)
        return (False, "")

    def longestDupSubstring(self, S):
        begin, end = 0, len(S)
        q = (1<<31) - 1 
        Found = ""
        while begin + 1 < end:
            mid = (begin + end)//2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                begin, Found = mid, candidate
            else:
                end = mid

        return Found